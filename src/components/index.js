
export default Vue.component("index", {
    template: `
	<main>
		<div class="page-banner home-banner">
			<div class="container h-100">
				<div class="row align-items-center h-100">
					<div class="col-lg-6 py-3 wow fadeInUp">
						<h1 class="mb-4">Great Companies are built on great Products</h1>
						<p class="text-lg mb-5">Ignite the most powerfull growth engine you have ever built for your
							company</p>

						<a href="#" class="btn btn-outline border text-secondary">More Info</a>
						<a href="#" class="btn btn-primary btn-split ml-2">Watch Video <div class="fab"><span
									class="mai-play"></span></div></a>
					</div>
					<div class="col-lg-6 py-3 wow zoomIn">
						<div class="img-place">
							<img src="assets/img/bg_image_1.png" alt="">
						</div>
					</div>
				</div>
				<a href="#about" class="btn-scroll" data-role="smoothscroll"><span class="mai-arrow-down"></span></a>
			</div>
		</div>
		<div class="page-section features">
			<div class="container">
				<div class="row justify-content-center">
					<div class="col-md-6 col-lg-4 py-3 wow fadeInUp">
						<div class="d-flex flex-row">
							<div class="img-fluid mr-3">
								<img src="assets/img/icon_pattern.svg" alt="">
							</div>
							<div>
								<h5>Provide financial advice by our advisor</h5>
								<p>Copywrite, blogpublic realations content translation.</p>
							</div>
						</div>
					</div>

					<div class="col-md-6 col-lg-4 py-3 wow fadeInUp">
						<div class="d-flex flex-row">
							<div class="img-fluid mr-3">
								<img src="assets/img/icon_pattern.svg" alt="">
							</div>
							<div>
								<h5>Complete solutions for global organisations</h5>
								<p>Copywrite, blogpublic realations content translation.</p>
							</div>
						</div>
					</div>

					<div class="col-md-6 col-lg-4 py-3 wow fadeInUp">
						<div class="d-flex flex-row">
							<div class="img-fluid mr-3">
								<img src="assets/img/icon_pattern.svg" alt="">
							</div>
							<div>
								<h5>Provide financial advice by our advisor</h5>
								<p>Copywrite, blogpublic realations content translation.</p>
							</div>
						</div>
					</div>
				</div>
			</div> <!-- .container -->
		</div> <!-- .page-section -->

		<div class="page-section">
			<div class="container">
			  <div class="row">
				<div class="col-lg-4">
				  <div class="card-service wow fadeInUp">
					<div class="header">
					  <img src="assets/img/services/service-1.svg" alt="">
					</div>
					<div class="body">
					  <h5 class="text-secondary">SEO Consultancy</h5>
					  <p>We help you define your SEO objective & develop a realistic strategy with you</p>
					  <a href="service.html" class="btn btn-primary">Read More</a>
					</div>
				  </div>
				</div>
				<div class="col-lg-4">
				  <div class="card-service wow fadeInUp">
					<div class="header">
					  <img src="assets/img/services/service-2.svg" alt="">
					</div>
					<div class="body">
					  <h5 class="text-secondary">Content Marketing</h5>
					  <p>We help you define your SEO objective & develop a realistic strategy with you</p>
					  <a href="service.html" class="btn btn-primary">Read More</a>
					</div>
				  </div>
				</div>
				<div class="col-lg-4">
				  <div class="card-service wow fadeInUp">
					<div class="header">
					  <img src="assets/img/services/service-3.svg" alt="">
					</div>
					<div class="body">
					  <h5 class="text-secondary">Keyword Research</h5>
					  <p>We help you define your SEO objective & develop a realistic strategy with you</p>
					  <a href="service.html" class="btn btn-primary">Read More</a>
					</div>
				  </div>
				</div>
			  </div>
			</div> <!-- .container -->
		  </div> <!-- .page-section -->

		<div class="page-section">
			<div class="container">
				<div class="row">
					<div class="col-lg-6 py-3 wow zoomIn">
						<div class="img-place text-center">
							<img src="assets/img/bg_image_2.png" alt="">
						</div>
					</div>
					<div class="col-lg-6 py-3 wow fadeInRight">
						<h2 class="title-section">We're <span class="marked">Dynamic</span> Team of Creatives People
						</h2>
						<div class="divider"></div>
						<p>We provide marketing services to startups & small business to looking for partner for their
							digital media, design & dev lead generation & communication.</p>
						<div class="img-place mb-3">
							<img src="assets/img/testi_image.png" alt="">
						</div>
						<a href="#" class="btn btn-primary">More Details</a>
						<a href="#" class="btn btn-outline border ml-2">Success Stories</a>
					</div>
				</div>
			</div> <!-- .container -->
		</div> <!-- .page-section -->

		<div class="page-section counter-section">
			<div class="container">
				<div class="row align-items-center text-center">
					<div class="col-lg-4">
						<p>Total Invest</p>
						<h2>$<span>816, 278</span></h2>
					</div>
					<div class="col-lg-4">
						<p>Yearly Revenue</p>
						<h2>$<span>216, 422</span></h2>
					</div>
					<div class="col-lg-4">
						<p>Growth Ration</p>
						<h2><span>73</span>%</h2>
					</div>
				</div>
			</div> <!-- .container -->
		</div> <!-- .page-section -->

		<div class="page-section">
			<div class="container">
				<div class="row">
					<div class="col-lg-6 py-3 wow fadeInLeft">
						<h2 class="title-section">We're <span class="marked">ready to</span> Serve you with best</h2>
						<div class="divider"></div>
						<p class="mb-5">We provide marketing services to startups & small business to looking for
							partner for their digital media, design & dev lead generation & communication.</p>
						<a href="#" class="btn btn-primary">More Details</a>
						<a href="#" class="btn btn-outline ml-2">See pricing</a>
					</div>
					<div class="col-lg-6 py-3 wow zoomIn">
						<div class="img-place text-center">
							<img src="assets/img/bg_image_3.png" alt="">
						</div>
					</div>
				</div>
			</div> <!-- .container -->
		</div> <!-- .page-section -->

		<!-- Banner info -->
		<div class="page-section banner-info">
			<div class="wrap bg-image" style="background-image: url(assets/img/bg_pattern.svg);">
			<div class="container">
				<div class="row align-items-center">
				<div class="col-lg-6 py-3 pr-lg-5 wow fadeInUp">
					<h2 class="title-section">SEO to Improve Brand <br> Visibility</h2>
					<div class="divider"></div>
					<p>We're an experienced and talented team of passionate consultants who breathe with search engine marketing.</p>
					
					<ul class="theme-list theme-list-light text-white">
					<li>
						<div class="h5">SEO Content Strategy</div>
						<p>Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor</p>
					</li>
					<li>
						<div class="h5">B2B SEO</div>
						<p>Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor</p>
					</li>
					</ul>
				</div>
				<div class="col-lg-6 py-3 wow fadeInRight">
					<div class="img-fluid text-center">
					<img src="assets/img/banner_image_2.svg" alt="">
					</div>
				</div>
				</div>
			</div>
			</div> <!-- .wrap -->
		</div> <!-- .page-section -->

		<div class="page-section">
			<div class="container">
				<div class="text-center wow fadeInUp">
					<div class="subhead">Why Choose Us</div>
					<h2 class="title-section">Your <span class="marked">Comfort</span> is Our Priority</h2>
					<div class="divider mx-auto"></div>
				</div>

				<div class="row mt-5 text-center">
					<div class="col-lg-4 py-3 wow fadeInUp">
						<div class="display-3"><span class="mai-shapes"></span></div>
						<h5>High Performance</h5>
						<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Laborum, sit.</p>
					</div>
					<div class="col-lg-4 py-3 wow fadeInUp">
						<div class="display-3"><span class="mai-shapes"></span></div>
						<h5>Friendly Prices</h5>
						<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Laborum, sit.</p>
					</div>
					<div class="col-lg-4 py-3 wow fadeInUp">
						<div class="display-3"><span class="mai-shapes"></span></div>
						<h5>No time-confusing</h5>
						<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Laborum, sit.</p>
					</div>
				</div>
			</div> <!-- .container -->
		</div> <!-- .page-section -->

		<div class="page-section border-top">
			<div class="container">
				<div class="text-center wow fadeInUp">
					<h2 class="title-section">Pricing Plan</h2>
					<div class="divider mx-auto"></div>
				</div>

				<div class="row justify-content-center">
					<div v-for="(item, index) in plans" :key="index" class="col-12 col-lg-auto py-3 wow fadeInLeft">
						<div v-if="item.rating > 5" class="card-pricing active">
							<div class="header">
								<div v-if="item.rating > 5" class="price-labled">Best</div>
								<div class="price-icon"><span :class="item.icon_cls"></span></div>
								<div class="price-title">{{item.title}}</div>
							</div>
							<div class="body py-3">
								<div class="price-tag">
									<span class="currency">$</span>
									<h2 class="display-4">{{item.price}}</h2>
									<span class="period">/monthly</span>
								</div>
								<div class="price-info">
									<p>{{item.detail}}</p>
								</div>
							</div>
							<div class="footer">
								<a href="#" class="btn btn-outline rounded-pill">Choose Plan</a>
							</div>
						</div>
						<div v-else class="card-pricing">
							<div class="header">
								<div class="price-icon"><span :class="item.icon_cls"></span></div>
								<div class="price-title">{{item.title}}</div>
							</div>
							<div class="body py-3">
								<div class="price-tag">
									<span class="currency">$</span>
									<h2 class="display-4">{{item.price}}</h2>
									<span class="period">/monthly</span>
								</div>
								<div class="price-info">
									<p>{{item.detail}}</p>
								</div>
							</div>
							<div class="footer">
								<a href="#" class="btn btn-outline rounded-pill">Choose Plan</a>
							</div>
						</div>
					</div>
				</div>
			</div> <!-- .container -->
		</div> <!-- .page-section -->

		<div class="page-section bg-light">
			<div class="container">

				<div class="owl-carousel wow fadeInUp" id="testimonials">
					<div class="item">
						<div class="row align-items-center">
							<div class="col-md-6 py-3">
								<div class="testi-image">
									<img src="assets/img/person/person_1.jpg" alt="">
								</div>
							</div>
							<div class="col-md-6 py-3">
								<div class="testi-content">
									<p>Necessitatibus ipsum magni accusantium consequatur delectus a repudiandae nemo
										quisquam dolorum itaque, tenetur, esse optio eveniet beatae explicabo sapiente
										quo.</p>
									<div class="entry-footer">
										<strong>Melvin Platje</strong> &mdash; <span class="text-grey">CEO Slurin
											Group</span>
									</div>
								</div>
							</div>
						</div>
					</div>

					<div class="item">
						<div class="row align-items-center">
							<div class="col-md-6 py-3">
								<div class="testi-image">
									<img src="assets/img/person/person_2.jpg" alt="">
								</div>
							</div>
							<div class="col-md-6 py-3">
								<div class="testi-content">
									<p>Repudiandae vero assumenda sequi labore ipsum eos ducimus provident a nam vitae
										et, dolorum temporibus inventore quaerat consectetur quos! Animi, qui ratione?
									</p>
									<div class="entry-footer">
										<strong>George Burke</strong> &mdash; <span class="text-grey">CEO Letro</span>
									</div>
								</div>
							</div>
						</div>
					</div>

				</div>
			</div> <!-- .container -->
		</div> <!-- .page-section -->

		<div class="page-section">
			<div class="container">
				<div class="row align-items-center">
					<div class="col-lg-6 py-3 wow fadeInUp">
						<h2 class="title-section">Get in Touch</h2>
						<div class="divider"></div>
						<p>Lorem ipsum dolor sit amet consectetur adipisicing elit.<br> Laborum ratione autem quidem
							veritatis!</p>

						<ul class="contact-list">
							<li>
								<div class="icon"><span class="mai-map"></span></div>
								<div class="content">123 Fake Street, New York, USA</div>
							</li>
							<li>
								<div class="icon"><span class="mai-mail"></span></div>
								<div class="content"><a href="#">info@digigram.com</a></div>
							</li>
							<li>
								<div class="icon"><span class="mai-phone-portrait"></span></div>
								<div class="content"><a href="#">+00 1122 3344 55</a></div>
							</li>
						</ul>
					</div>
					<div class="col-lg-6 py-3 wow fadeInUp">
						<div class="subhead">Contact Us</div>
						<h2 class="title-section">Drop Us a Line</h2>
						<div class="divider"></div>

						<form action="#">
							<div class="py-2">
								<input type="text" class="form-control" placeholder="Full name">
							</div>
							<div class="py-2">
								<input type="text" class="form-control" placeholder="Email">
							</div>
							<div class="py-2">
								<textarea rows="6" class="form-control" placeholder="Enter message"></textarea>
							</div>
							<button type="submit" class="btn btn-primary rounded-pill mt-4">Send Message</button>
						</form>
					</div>
				</div>
			</div> <!-- .container -->
		</div> <!-- .page-section -->

		<div class="page-section border-top">
			<div class="container">
				<div class="text-center wow fadeInUp">
					<div class="subhead">Our Blog</div>
					<h2 class="title-section">Read our latest <span class="marked">News</span></h2>
					<div class="divider mx-auto"></div>
				</div>

				<div class="row my-5 card-blog-row">
					<div v-for="(item, index) in posts" :key="index" class="col-md-6 col-lg-3 py-3 wow fadeInUp">
						<div class="card-blog">
							<div class="header">
								<div class="avatar">
									<img src="assets/img/person/person_3.jpg" alt="">
								</div>
								<div class="entry-footer">
									<div class="post-author">Sam Newman</div>
									<a href="#" class="post-date">{{item.date}}</a>
								</div>
							</div>
							<div class="body">
								<div class="post-title">
									<router-link :to="'/blog/'+item.title.replace(/ /g, '_')">{{item.title}}
									</router-link>
								</div>
								<div class="post-excerpt">{{item.body.slice(0, 75)}}...</div>
							</div>
							<div class="footer">
								<router-link :to="'/blog/'+item.title.replace(/ /g, '_')">Read More <span
										class="mai-chevron-forward text-sm"></span></router-link>
							</div>
						</div>
					</div>
				</div>

				<div class="text-center">
					<router-link to="/blog" class="btn btn-outline-primary rounded-pill">Discover More</router-link>
				</div>
			</div> <!-- .container -->
		</div> <!-- .page-section -->

		<div class="page-section client-section">
			<div class="container-fluid">
				<div class="row row-cols-2 row-cols-md-3 row-cols-lg-5 justify-content-center">
					<div class="item wow zoomIn">
						<img src="assets/img/clients/airbnb.png" alt="">
					</div>
					<div class="item wow zoomIn">
						<img src="assets/img/clients/google.png" alt="">
					</div>
					<div class="item wow zoomIn">
						<img src="assets/img/clients/stripe.png" alt="">
					</div>
					<div class="item wow zoomIn">
						<img src="assets/img/clients/paypal.png" alt="">
					</div>
					<div class="item wow zoomIn">
						<img src="assets/img/clients/mailchimp.png" alt="">
					</div>
				</div>
			</div> <!-- .container-fluid -->
		</div> <!-- .page-section -->
	</main>
`,
		data() {
			return {
				posts: [],
				plans: []
			}
		},
		mounted() {
			fetch("http://localhost:9999/api/posts?limit=4").then(data => data.json())
			.then((data) => {
				data = data.data
				for (var i in data) {
					var date = data[i].date.split("-");
					data[i].date = new Date(date[0], date[1], date[2]).toDateString()
					this.posts.push(data[i])
				}
			})
			fetch("http://localhost:9999/api/plans").then(data => data.json())
			.then((data) => {
				this.plans = data.data
			})
		}
	}
)
