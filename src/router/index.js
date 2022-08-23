
import index from '../components/index.js'
import blog from '../components/blog2.js'
import about from '../components/about.js'
import contact from '../components/contact.js'
import services from '../components/services.js'
import single from '../components/blog-single.js'
import search from '../components/search.js'

// Vue.use(Router)
export default new VueRouter({
  routes: [
    {
      path: '/',
      name: 'home',
      component: index
    },
    {
      path: '/blog',
      name: 'blog',
      component: blog,
	  props: (route) => ({curpage: route.query.page, query: route.query.q})
    },
    {
      path: '/search',
      name: 'search',
      component: search,
	  props: (route) => ({query: route.query.q})
    },
    {
      path: '/about',
      name: 'about',
      component: about
    },
    {
      path: '/contact',
      name: 'contact',
      component: contact
    },
    {
      path: '/services',
      name: 'services',
      component: services
    },
	{
		path: '/blog/:id',
		name: 'single',
		component: single,
		props: true
	  },
  ],
  scrollBehavior (to, from, savedPosition ) {
	if ( savedPosition ) {
		return savedPosition
	} else if (to.hash) {
		return {
			el: to.hash,
			behavior: 'smooth'
		}
	} else {
		return {
			el: document.getElementsByTagName("main")[0]
		}
	}
  },
})

