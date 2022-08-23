import paginate from "./Paginate.js"

export default Vue.component("blog", {
    template: `
	<main>
		<div class="page-section">
			<div class="container">
				<div class="col">
					<form action="#" class="form-search-blog">
						<div class="input-group">
						<div class="input-group-prepend">
							<select id="categories" class="custom-select bg-light">
							<option>Categories</option>
							<option value="travel">Travel</option>
							<option value="lifestyle">LifeStyle</option>
							<option value="healthy">Healthy</option>
							<option value="food">Food</option>
							</select>
						</div>
						<input type="text" id="search" class="form-control" placeholder="Enter keyword.." :value="$route.query.keyword || ''">
						</div>
					</form>
					</div>
				<!--  <div class="col-sm-2 text-sm-right">
					<button class="btn btn-secondary">Filter <span class="mai-filter"></span></button>
					</div> -->

				<div class="row">
					<template v-if="ready && posts.length > 0">
					<div v-for="(item, index) in posts" :key="index" class="col-md-6 col-lg-4 py-3">
						<div class="card-blog">
							<div class="header">
								<div class="avatar">
									<img src="assets/img/person/person_1.jpg" alt="">
								</div>
								<div class="entry-footer">
									<div class="post-author">Sam Newman</div>
									<a href="#" class="post-date">{{ to_date_str(item.date) }}</a>
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
					</template>
					<template v-else >
						<div class="col-md-12 col-lg-12 py-3"">
							<center><h3>No Posts</h3></center>
						</div>
					</template>
					<div class="col-12 mt-5">
						<nav aria-label="Page Navigation">
							<paginate
								v-model="page"
								:pageCount="pagesnum"
								:clickHandler="get_page_content"
								:prev-text="'Previous'"
								:next-text="'Next'"
								:container-class="'pagination justify-content-center'"
								:page-range="3"
								:prev-class="'page-link'"
								:next-class="'page-link'"
								:active-class="'page-item active primary'"
								page-class="page-link"
								:hide-prev-next="true"
								:margin-pages="1" >
							</paginate>
						</nav>
					</div>

				</div>

			</div>
		</div>
	</main>
`,
		props: ["curpage", "query"],
		data() {
			return {
				posts: [],
				pagesnum: 0,
				page: this.curpage != undefined ? new Number(this.curpage) : 1,
				ready: false
			}
		},
		methods: {
			get_page_content(pagenum) {
				var from = 1;
				var to = 9;
				var perpage = 9;

				this.page = pagenum;
				this.$route.query.page = this.page;

				for (var i = 0; i < this.page - 1; i++) {
					from += perpage;
					 to += perpage;
				}
				
				if (this.$route.query.keyword) {
					if (this.$route.query.keyword != "") {
						$("#search").val(this.$route.query.keyword)
						fetch(`http://localhost:9999/api/posts?keyword=${this.$route.query.keyword}&from=${from}&to=${to}`)
						.then(data => data.json())
						.then((data) => {
							this.posts = data.data
							this.pagesnum = Math.ceil(new Number(data.total) / 9)
						})
					} else {
						this.$router.push({name: "blog"})
					}
				} else {
					fetch(`http://localhost:9999/api/posts?from=${from}&to=${to}`)
					.then(data => data.json())
					.then((data) => {
						this.posts = data.data
			console.log(this.posts)
						this.pagesnum = Math.ceil(new Number(data.total) / 9)
					})
				}
			},
			to_date_str(date) {
				var date = date.split("-");
				return new Date(date[0], date[1], date[2]).toDateString()
			}
		},
		mounted() {
			this.get_page_content(this.page);
			this.ready = true;

			$("#search").on("change paste keyup", () => {
				var val = $("#search").val();
				if (this.$route.query.keyword !== val) {
					this.$router.push({name: "blog", query: {keyword: val}});
					this.get_page_content(1);
				}
			})
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