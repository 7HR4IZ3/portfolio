import top from './components/base/Header.js';

import foot from './components/base/Footer.js';

// import "../assets/vendor/waypoints/jquery.waypoints.min.js";
// import "../assets/vendor/animateNumber/jquery.animateNumber.min.js";

export default Vue.component("App", {
    template: `
  <section id="app">
      <!-- Back to top button -->
    <div class="back-to-top"></div>
    <top></top>
    <router-view :key="$route.path"></router-view>
    <foot></foot>
  </section>
`,
  components: {
		top, foot
  },
  mounted() {
	setInterval(() => {
		this.$forceUpdate();
	}, 500);
  }
})