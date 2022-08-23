SystemJS.config({
  baseURL:'res/',
  defaultExtension: true,
  meta: {
    '*.vue': {
      'loader': 'vue-loader'
    }
  },
  map: {
    'plugin-babel': 'plugin-babel.js',
    'systemjs-babel-build': 'systemjs-babel-browser.js',
    'vue-loader': 'systemjs-vue-loader.js',
    'vue-router': 'vue-router.js',
    'vue': 'vue.js',
    'vue-template-compiler': 'browser.js'
  },
  transpiler: 'plugin-babel'
});

SystemJS.import('./src/main.js').catch(console.error.bind(console));