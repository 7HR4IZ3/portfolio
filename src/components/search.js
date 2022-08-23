import paginate from "./Paginate.js"

export default Vue.component("blog", {
    template: `
	<main>
		<div class="page-section">
			<div class="container">
				<div class="row">
					<div class="col-sm-10">
						<form action="#" class="form-search-blog">
						  <div class="input-group">
							<div class="input-group-prepend">
							  <select id="categories" class="custom-select bg-light">
								<option>All Categories</option>
								<option value="travel">Travel</option>
								<option value="lifestyle">LifeStyle</option>
								<option value="healthy">Healthy</option>
								<option value="food">Food</option>
							  </select>
							</div>
							<input type="text" class="form-control" placeholder="Enter keyword..">
						  </div>
						</form>
					  </div>
					  <div class="col-sm-2 text-sm-right">
						<button class="btn btn-secondary">Filter <span class="mai-filter"></span></button>
					  </div>
					<div v-for="(item, index) in posts" :key="index" class="col-md-6 col-lg-4 py-3">
						<div class="card-blog">
							<div class="header">
								<div class="avatar">
									<img src="assets/img/person/person_1.jpg" alt="">
								</div>
								<div class="entry-footer">
									<div class="post-author">Sam Newman</div>
									<a href="#" class="post-date">23 Apr 2020</a>
								</div>
							</div>
							<div class="body">
								<div class="post-title">
									<router-link :to="'/blog/'+item.title.replace(/ /g, '_')">{{item.title}}
									</router-link>
								</div>
								<div class="post-excerpt">{{item.body.slice(0, 70)}}.</div>
							</div>
							<div class="footer">
								<router-link :to="'/blog/'+item.title.replace(/ /g, '_')">Read More <span
										class="mai-chevron-forward text-sm"></span></router-link>
							</div>
						</div>
					</div>
					<div class="col-12 mt-5">
						<nav aria-label="Page Navigation">
							<paginate
								v-model="page"
								:pageCount="pagesnum"
								:clickHandler="getPageContent"
								:prev-text="'Previous'"
								:next-text="'Next'"
								:container-class="'pagination justify-content-center'"
								:page-range="2"
								:prev-class="'page-link'"
								:next-class="'page-link'"
								:active-class="'page-item active'"
								page-class="page-link"
								:hide-prev-next="true"
								:margin-pages="2" >
							</paginate>
						</nav>
					</div>

				</div>

			</div>
		</div>
	</main>
`,
		props: ["curpage"],
		data() {
			return {
				posts: [],
				pagesnum: 0,
				page: this.curpage != undefined ? this.curpage : 1
			}
		},
		methods: {
			getPageContent(pagenum) {
				var from = 1;
				var to = 9;
				var perpage = 9;

				this.page = pagenum;
				this.$route.query.page = this.page;

				for (var i = 0; i < this.page - 1; i++) {
					from += perpage;
					to += perpage;
				}

				fetch(`http://localhost:9999/api/posts?from=${from}&to=${to}`)
				.then(data => data.json())
				.then((data) => {
					this.posts = []
					for (var i in data) {
						this.posts.push(data[i])
					}
					this.$forceUpdate()
				})
			}
		},
		mounted() {
			fetch("http://localhost:9999/api/posts/length")
			.then(data => data.json())
			.then((data) => {
				this.pagesnum = Math.ceil(new Number(data) / 9)
			})
			this.getPageContent(this.page)

		}
	}
)

/* <ul class="pagination justify-content-center">
<li class="page-item disabled">
	<router-link v-if="page > 1" class="page-link" :to="{query: {page: page - 1} }" >Previous</router-link>
</li>

<div v-for="num in pagesnum" :key="num">
	<li v-if="num == page" class="page-item active" aria-current="page">
		<router-link class="page-link" :to="{query: {page: num} }">{{num}}</router-link>
	</li>
	<li v-else class="page-item"><router-link class="page-link" :to="{query: {page: num} }">{{num}}</router-link></li>
</div>

<li class="page-item">
	<router-link v-if="page < pagesnum" class="page-link" :to="{query: {page: page + 1} }">Next</router-link>
</li>
</ul> */