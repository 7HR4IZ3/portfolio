
export default Vue.component("bc", {
    template: `
    <div class="container mt-5">
        <div class="page-banner">
          <div class="row justify-content-center align-items-center">
            <div class="col-md-6">
              <nav aria-label="Breadcrumb">
                <ul class="breadcrumb justify-content-center py-0 bg-transparent">
                  <li class="breadcrumb-item"><router-link to="/">Home</router-link></li>
                  <li class="breadcrumb-item active">News</li>
                </ul>
              </nav>
              <h1 class="text-center">News</h1>
            </div>
          </div>
        </div>
    </div>
`,

	}
)
