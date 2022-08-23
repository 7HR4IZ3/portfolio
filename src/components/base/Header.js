import bc from './breadcrumbs.js';

export default Vue.component("top", {
    template: `
  <header class="sticky-top">
    <nav class="navbar navbar-expand-lg navbar-light shadow-sm" style="background-color: white">
      <div class="container">
        <router-link to="/" class="navbar-brand">Elip<span class="text-primary">sis.</span></router-link>

        <button class="navbar-toggler" data-toggle="collapse" data-target="#navbarContent" aria-controls="navbarContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="navbar-collapse collapse" id="navbarContent">
          <ul class="navbar-nav ml-lg-4 pt-3 pt-lg-0">
            <li class="nav-item">
              <router-link to="/" class="nav-link">Home</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/about" class="nav-link">About</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/services" class="nav-link">Services</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/blog" class="nav-link">News</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/contact" class="nav-link">Contact</router-link>
            </li>
          </ul>

          <div class="ml-auto">
            <a href="#" class="btn btn-outline rounded-pill">Get a Quote</a>
          </div>
        </div>
      </div>
    </nav>
    <!-- <bc /> -->
  </header>
`,
    components: {bc}
	}
)
