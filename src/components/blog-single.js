export default Vue.component("top", {
    template: `
	<main>
		<div class="page-section pt-5">
			<div class="container">
				<nav aria-label="Breadcrumb">
					<ul class="breadcrumb p-0 mb-0 bg-transparent">
						<li class="breadcrumb-item">
							<router-link to="{name: 'index'}">Home</router-link>
						</li>
						<li class="breadcrumb-item">
							<router-link to="{name: 'blog'}">Blog</router-link>
						</li>
						<li class="breadcrumb-item active">{{item.title}}</li>
					</ul>
				</nav>

				<div class="row">
					<div class="col-lg-8">
						<div class="blog-single-wrap">
							<div class="header">
								<div class="post-thumb">
								<img src="assets/img/blog/blog-1.jpg" alt="">
								</div>
								<div class="meta-header">
									<div class="post-author">
										<div class="avatar">
											<img src="assets/img/person/person_1.jpg" alt="">
										</div>
										by <a href="#">Stephen Doe</a>
									</div>

									<div class="post-sharer">
										<a href="#" class="btn social-facebook"><span
												class="mai-logo-facebook-f"></span></a>
										<a href="#" class="btn social-twitter"><span
												class="mai-logo-twitter"></span></a>
										<a href="#" class="btn social-linkedin"><span
												class="mai-logo-linkedin"></span></a>
										<a href="#" class="btn"><span class="mai-mail"></span></a>
									</div>
								</div>
							</div>
							<h1 class="post-title">{{item.title}}</h1>
							<div class="post-meta">
								<div class="post-date">
									<span class="icon">
										<span class="mai-time-outline"></span>
									</span> <a href="#">{{ to_date_str(item.date) }}</a>
								</div>
								<div class="post-comment-count ml-2">
									<span class="icon">
										<span class="mai-chatbubbles-outline"></span>
									</span> <a href="#">4 Comments</a>
								</div>
							</div>
							<div class="post-content">
								<p>{{item.body[0]}}</p>
								<p>{{item.body[1]}}</p>
								<blockquote class="quote">“I'm selfish, impatient and a little insecure. I make
									mistakes, I am out of control and at times hard to handle. But if you can't handle
									me at my worst, then you sure as hell don't deserve me at my best.”
									<span class="author">― Marilyn Monroe</span></blockquote>
								<p v-for="(body, index) in item.body.slice(2)" :key="index">
									{{body}}</p>
							</div>
						</div>

						<div class="comment-form-wrap pt-5">
							<h2 class="mb-5">Leave a comment</h2>
							<form action="#" class="">
								<div class="form-row form-group">
									<div class="col-md-6">
										<label for="name">Name *</label>
										<input type="text" class="form-control" id="name">
									</div>
									<div class="col-md-6">
										<label for="email">Email *</label>
										<input type="email" class="form-control" id="email">
									</div>
								</div>
								<div class="form-group">
									<label for="website">Website</label>
									<input type="url" class="form-control" id="website">
								</div>

								<div class="form-group">
									<label for="message">Message</label>
									<textarea name="msg" id="message" cols="30" rows="8"
										class="form-control"></textarea>
								</div>
								<div class="form-group">
									<input type="submit" value="Post Comment" class="btn btn-primary">
								</div>

							</form>
						</div>

					</div>
					<div class="col-lg-4">
						<div class="widget">
							<!-- Widget search -->
							<div class="widget-box">
								<div class="search-widget">
									<input type="text" name="keyword" id="search_text" class="form-control" placeholder="Enter keyword..">
									<button id="search_submit" class="btn btn-primary btn-block" @click="search()">Search</button>
								</div>
							</div>

							<!-- Widget Categories -->
							<div class="widget-box">
								<h4 class="widget-title">Category</h4>
								<div class="divider"></div>

								<ul class="categories">
									<li v-for="(category, index) in item.category.split(',')" :key="index"><a href="#">{{ category }}</a></li>
								</ul>
							</div>

							<!-- Widget recent post -->
							<div class="widget-box">
								<h4 class="widget-title">Recent Post</h4>
								<div class="divider"></div>

								<div v-for="(post, index) in posts" :key="index" class="blog-item">
									<router-link class="post-thumb" :to="'/blog/'+post.title.replace(/ /g, '_')"></router-link>
										<img :src="'assets/img/'+post.image" alt="">
									</router-link>
									<div class="content">
										<h6 class="post-title">
											<router-link :to="'/blog/'+post.title.replace(/ /g, '_')">{{post.title}}</router-link>
										</h6>
										<div class="meta">
											<a href="#"><span class="mai-calendar"></span> {{ to_date_str(post.date) }}</a>
											<a href="#"><span class="mai-person"></span> Admin</a>
											<a href="#"><span class="mai-chatbubbles"></span> 19</a>
										</div>
									</div>
								</div>
							</div>

							<!-- Widget Tag Cloud -->
							<div class="widget-box">
								<h4 class="widget-title">Tag Cloud</h4>
								<div class="divider"></div>

								<div class="tag-clouds">
									<a v-for="(t, index) in item.tag.split(',')" :key="index" href="#" class="tag-cloud-link">{{ t }}</a>
								</div>
							</div>

						</div>
					</div>
				</div>

			</div>
		</div>
	</main>`,
		props: ["id"],
		data() {
			return {
				item: {},
				posts: []
			}
		},
		methods: {
			to_date_str(date) {
				var date = date.split("-");
				return new Date(date[0], date[1], date[2]).toDateString()
			},
			search() {
				console.log('search')
				this.$router.push({name: "blog", query: {keyword: $("#search_text").val()}})
			}
		},
		mounted() {
			fetch("http://localhost:9999/api/posts?title=" + this.id.replace(/_/g, " ")).then(data => data.json())
			.then((data) => {
				this.item = data[0]
				this.item.body = this.item.body.split("/nl/")
			})
			
			fetch("http://localhost:9999/api/posts/random/4").then(data => data.json())
			.then((data) => {
				this.posts = data
			})
		}
	}
)