<template>
  <!DOCTYPE html>
  <html lang="en">

  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, shrink-to-fit=no">
    <title>Untitled</title>

  </head>

  <body>
  <HeaderComp/>
  <section class="newsletter-subscribe py-4 py-xl-5">
    <div class="container">
      <div class="row mb-2">
        <div class="col-md-8 col-xl-6 text-center mx-auto">
          <h2 class="display-6 fw-bold">Library Search</h2>
          <p class="text-muted">JJust start typing the problem that interests you, and the most suitable options will
            appear in the drop-down list.</p>
        </div>
      </div>
      <div class="d-flex justify-content-center flex-wrap">
        <div id="lib_search_input" class="position-relative mb-3">
          <div class="input-group" style="width: auto;">
            <input type="text" id="search_input" class="form-control"
                   aria-label="Recipient's username" aria-describedby="basic-addon3" @blur="hideList" @focus="showList"
                   @input="onEnterSearch"
                   @keyup.enter="GoToSearch" name="search" autocomplete="off"
                   placeholder="How to read a file">
            <button class="input-group-text btn btn-primary" id="basic-addon3" @click="GoToSearch">Go!</button>
          </div>

          <div v-if="search_tip" id='tipslist' @mouseover="canClosed = false" @mouseleave="canClosed = true"
               class="shadow-lg position-absolute padding-top-xs list-group"
               style="border: 0 solid #0a53be; margin-top: .5em; width: 100%;">
            <button v-for="tip of search_tip"
               class='list-group-item list-group-item-action d-flex justify-content-between'
               @click="GoToTip(tip.urlHash)">
              <div style='width: fit-content;'>
                {{ tip.heading }}
              </div>
              <div class="d-flex row" style='width: fit-content;'>
                <div v-for="tag of tip.tags" style='width: fit-content;'>
                  <div v-if="tag.icon">
                    <img style="width: 20px;" :src="'http://' + backend + tag.icon">
                  </div>
                  <div v-else-if="tag.name">
                    {{ tag.name }}
                  </div>
                </div>
              </div>
            </button>

            <button class='list-group-item list-group-item-action d-flex justify-content-between' @click="$router.push('search')">
              <div style='width: fit-content; display: flex; align-items: center;'>
                View all offers&thinsp;
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                     class="bi bi-arrow-right" viewBox="0 0 16 16">
                  <path fill-rule="evenodd"
                        d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8z"/>
                </svg>
              </div>
            </button>

          </div>
        </div>
      </div>
    </div>
    <div class="container py-4 py-xl-5">
      <div class="row gy-4 row-cols-2 row-cols-md-4">
        <div class="col">
          <div class="text-center d-flex flex-column justify-content-center align-items-center py-3">
            <div
                class="bs-icon-xl bs-icon-circle bs-icon-primary d-flex flex-shrink-0 justify-content-center align-items-center d-inline-block mb-2 bs-icon lg">
              <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" viewBox="0 0 16 16"
                   class="bi bi-bell">
                <path
                    d="M8 16a2 2 0 0 0 2-2H6a2 2 0 0 0 2 2zM8 1.918l-.797.161A4.002 4.002 0 0 0 4 6c0 .628-.134 2.197-.459 3.742-.16.767-.376 1.566-.663 2.258h10.244c-.287-.692-.502-1.49-.663-2.258C12.134 8.197 12 6.628 12 6a4.002 4.002 0 0 0-3.203-3.92L8 1.917zM14.22 12c.223.447.481.801.78 1H1c.299-.199.557-.553.78-1C2.68 10.2 3 6.88 3 6c0-2.42 1.72-4.44 4.005-4.901a1 1 0 1 1 1.99 0A5.002 5.002 0 0 1 13 6c0 .88.32 4.2 1.22 6z"></path>
              </svg>
            </div>
            <div class="px-3">
              <h2 class="fw-bold mb-0">123+</h2>
              <p class="mb-0">Erat netus</p>
            </div>
          </div>
        </div>
        <div class="col">
          <div class="text-center d-flex flex-column justify-content-center align-items-center py-3">
            <div
                class="bs-icon-xl bs-icon-circle bs-icon-primary d-flex flex-shrink-0 justify-content-center align-items-center d-inline-block mb-2 bs-icon lg">
              <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" viewBox="0 0 16 16"
                   class="bi bi-bezier">
                <path fill-rule="evenodd"
                      d="M0 10.5A1.5 1.5 0 0 1 1.5 9h1A1.5 1.5 0 0 1 4 10.5v1A1.5 1.5 0 0 1 2.5 13h-1A1.5 1.5 0 0 1 0 11.5v-1zm1.5-.5a.5.5 0 0 0-.5.5v1a.5.5 0 0 0 .5.5h1a.5.5 0 0 0 .5-.5v-1a.5.5 0 0 0-.5-.5h-1zm10.5.5A1.5 1.5 0 0 1 13.5 9h1a1.5 1.5 0 0 1 1.5 1.5v1a1.5 1.5 0 0 1-1.5 1.5h-1a1.5 1.5 0 0 1-1.5-1.5v-1zm1.5-.5a.5.5 0 0 0-.5.5v1a.5.5 0 0 0 .5.5h1a.5.5 0 0 0 .5-.5v-1a.5.5 0 0 0-.5-.5h-1zM6 4.5A1.5 1.5 0 0 1 7.5 3h1A1.5 1.5 0 0 1 10 4.5v1A1.5 1.5 0 0 1 8.5 7h-1A1.5 1.5 0 0 1 6 5.5v-1zM7.5 4a.5.5 0 0 0-.5.5v1a.5.5 0 0 0 .5.5h1a.5.5 0 0 0 .5-.5v-1a.5.5 0 0 0-.5-.5h-1z"></path>
                <path
                    d="M6 4.5H1.866a1 1 0 1 0 0 1h2.668A6.517 6.517 0 0 0 1.814 9H2.5c.123 0 .244.015.358.043a5.517 5.517 0 0 1 3.185-3.185A1.503 1.503 0 0 1 6 5.5v-1zm3.957 1.358A1.5 1.5 0 0 0 10 5.5v-1h4.134a1 1 0 1 1 0 1h-2.668a6.517 6.517 0 0 1 2.72 3.5H13.5c-.123 0-.243.015-.358.043a5.517 5.517 0 0 0-3.185-3.185z"></path>
              </svg>
            </div>
            <div class="px-3">
              <h2 class="fw-bold mb-0">45+</h2>
              <p class="mb-0">Erat netus</p>
            </div>
          </div>
        </div>
        <div class="col">
          <div class="text-center d-flex flex-column justify-content-center align-items-center py-3">
            <div
                class="bs-icon-xl bs-icon-circle bs-icon-primary d-flex flex-shrink-0 justify-content-center align-items-center d-inline-block mb-2 bs-icon lg">
              <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" viewBox="0 0 16 16"
                   class="bi bi-cup">
                <path
                    d="M1 2a1 1 0 0 1 1-1h11a1 1 0 0 1 1 1v1h.5A1.5 1.5 0 0 1 16 4.5v7a1.5 1.5 0 0 1-1.5 1.5h-.55a2.5 2.5 0 0 1-2.45 2h-8A2.5 2.5 0 0 1 1 12.5V2zm13 10h.5a.5.5 0 0 0 .5-.5v-7a.5.5 0 0 0-.5-.5H14v8zM13 2H2v10.5A1.5 1.5 0 0 0 3.5 14h8a1.5 1.5 0 0 0 1.5-1.5V2z"></path>
              </svg>
            </div>
            <div class="px-3">
              <h2 class="fw-bold mb-0">67+</h2>
              <p class="mb-0">Erat netus</p>
            </div>
          </div>
        </div>
        <div class="col">
          <div class="text-center d-flex flex-column justify-content-center align-items-center py-3">
            <div
                class="bs-icon-xl bs-icon-circle bs-icon-primary d-flex flex-shrink-0 justify-content-center align-items-center d-inline-block mb-2 bs-icon lg">
              <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" viewBox="0 0 16 16"
                   class="bi bi-cart2">
                <path
                    d="M0 2.5A.5.5 0 0 1 .5 2H2a.5.5 0 0 1 .485.379L2.89 4H14.5a.5.5 0 0 1 .485.621l-1.5 6A.5.5 0 0 1 13 11H4a.5.5 0 0 1-.485-.379L1.61 3H.5a.5.5 0 0 1-.5-.5zM3.14 5l1.25 5h8.22l1.25-5H3.14zM5 13a1 1 0 1 0 0 2 1 1 0 0 0 0-2zm-2 1a2 2 0 1 1 4 0 2 2 0 0 1-4 0zm9-1a1 1 0 1 0 0 2 1 1 0 0 0 0-2zm-2 1a2 2 0 1 1 4 0 2 2 0 0 1-4 0z"></path>
              </svg>
            </div>
            <div class="px-3">
              <h2 class="fw-bold mb-0">89</h2>
              <p class="mb-0">Erat netus</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
  <div class="container py-4 py-xl-5">
    <div class="row mb-5">
      <div class="col-md-8 col-xl-6 text-center mx-auto">
        <h2>Heading</h2>
        <p class="w-lg-50">Curae hendrerit donec commodo hendrerit egestas tempus, turpis facilisis nostra nunc.
          Vestibulum dui eget ultrices.</p>
      </div>
    </div>
    <div class="row gy-4 row-cols-1 row-cols-md-2 row-cols-xl-3 d-xl-flex">
      <div class="col">
        <div class="card mb-4">
          <div class="card-body text-center p-4">
            <h4 class="fw-bold card-subtitle">Free</h4>
            <h4 class="display-5 fw-bold card-title">$0</h4>
            <p>Non vulputate feugiat semper.</p><a class="btn btn-light d-block w-100" role="button" href="#">Button</a>
          </div>
        </div>
        <div class="bg-light border rounded border-light p-4">
          <ul class="list-unstyled">
            <li class="d-flex mb-2"><span class="bs-icon-xs bs-icon-rounded bs-icon-primary-light bs-icon me-2"><svg
                xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" viewBox="0 0 16 16"
                class="bi bi-check-lg text-primary">
                                    <path
                                        d="M12.736 3.97a.733.733 0 0 1 1.047 0c.286.289.29.756.01 1.05L7.88 12.01a.733.733 0 0 1-1.065.02L3.217 8.384a.757.757 0 0 1 0-1.06.733.733 0 0 1 1.047 0l3.052 3.093 5.4-6.425a.247.247 0 0 1 .02-.022Z"></path>
                                </svg></span><span>Lectus ut nibh quam, felis porttitor.</span></li>
            <li class="d-flex mb-2"><span class="bs-icon-xs bs-icon-rounded bs-icon-primary-light bs-icon me-2"><svg
                xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" viewBox="0 0 16 16"
                class="bi bi-check-lg text-primary">
                                    <path
                                        d="M12.736 3.97a.733.733 0 0 1 1.047 0c.286.289.29.756.01 1.05L7.88 12.01a.733.733 0 0 1-1.065.02L3.217 8.384a.757.757 0 0 1 0-1.06.733.733 0 0 1 1.047 0l3.052 3.093 5.4-6.425a.247.247 0 0 1 .02-.022Z"></path>
                                </svg></span><span>Ante nec venenatis etiam lacinia.</span></li>
            <li class="d-flex mb-2"><span class="bs-icon-xs bs-icon-rounded bs-icon-primary-light bs-icon me-2"><svg
                xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" viewBox="0 0 16 16"
                class="bi bi-check-lg text-primary">
                                    <path
                                        d="M12.736 3.97a.733.733 0 0 1 1.047 0c.286.289.29.756.01 1.05L7.88 12.01a.733.733 0 0 1-1.065.02L3.217 8.384a.757.757 0 0 1 0-1.06.733.733 0 0 1 1.047 0l3.052 3.093 5.4-6.425a.247.247 0 0 1 .02-.022Z"></path>
                                </svg></span><span>Porta suscipit netus ad ac.</span></li>
          </ul>
        </div>
      </div>
      <div class="col">
        <div class="card border-primary border-2 mb-4">
          <div class="card-body text-center p-4"><span
              class="badge rounded-pill bg-primary position-absolute top-0 start-50 translate-middle text-uppercase">Most Popular</span>
            <h4 class="fw-bold card-subtitle">Pro</h4>
            <h4 class="display-5 fw-bold card-title">$38<span class="fs-4 fw-normal text-muted">/mo</span></h4>
            <p>Varius rutrum duis vel.</p><a class="btn btn-primary d-block w-100" role="button" href="#">Button</a>
          </div>
        </div>
        <div class="bg-light border rounded border-light p-4">
          <ul class="list-unstyled">
            <li class="d-flex mb-2"><span class="bs-icon-xs bs-icon-rounded bs-icon-primary-light bs-icon me-2"><svg
                xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" viewBox="0 0 16 16"
                class="bi bi-check-lg text-primary">
                                    <path
                                        d="M12.736 3.97a.733.733 0 0 1 1.047 0c.286.289.29.756.01 1.05L7.88 12.01a.733.733 0 0 1-1.065.02L3.217 8.384a.757.757 0 0 1 0-1.06.733.733 0 0 1 1.047 0l3.052 3.093 5.4-6.425a.247.247 0 0 1 .02-.022Z"></path>
                                </svg></span><span>Lectus ut nibh quam, felis porttitor.</span></li>
            <li class="d-flex mb-2"><span class="bs-icon-xs bs-icon-rounded bs-icon-primary-light bs-icon me-2"><svg
                xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" viewBox="0 0 16 16"
                class="bi bi-check-lg text-primary">
                                    <path
                                        d="M12.736 3.97a.733.733 0 0 1 1.047 0c.286.289.29.756.01 1.05L7.88 12.01a.733.733 0 0 1-1.065.02L3.217 8.384a.757.757 0 0 1 0-1.06.733.733 0 0 1 1.047 0l3.052 3.093 5.4-6.425a.247.247 0 0 1 .02-.022Z"></path>
                                </svg></span><span>Ante nec venenatis etiam lacinia.</span></li>
            <li class="d-flex mb-2"><span class="bs-icon-xs bs-icon-rounded bs-icon-primary-light bs-icon me-2"><svg
                xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" viewBox="0 0 16 16"
                class="bi bi-check-lg text-primary">
                                    <path
                                        d="M12.736 3.97a.733.733 0 0 1 1.047 0c.286.289.29.756.01 1.05L7.88 12.01a.733.733 0 0 1-1.065.02L3.217 8.384a.757.757 0 0 1 0-1.06.733.733 0 0 1 1.047 0l3.052 3.093 5.4-6.425a.247.247 0 0 1 .02-.022Z"></path>
                                </svg></span><span>Porta suscipit netus ad ac.</span></li>
            <li class="d-flex mb-2"><span class="bs-icon-xs bs-icon-rounded bs-icon-primary-light bs-icon me-2"><svg
                xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" viewBox="0 0 16 16"
                class="bi bi-check-lg text-primary">
                                    <path
                                        d="M12.736 3.97a.733.733 0 0 1 1.047 0c.286.289.29.756.01 1.05L7.88 12.01a.733.733 0 0 1-1.065.02L3.217 8.384a.757.757 0 0 1 0-1.06.733.733 0 0 1 1.047 0l3.052 3.093 5.4-6.425a.247.247 0 0 1 .02-.022Z"></path>
                                </svg></span><span>Morbi praesent aptent integer at.</span></li>
            <li class="d-flex mb-2"><span class="bs-icon-xs bs-icon-rounded bs-icon-primary-light bs-icon me-2"><svg
                xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" viewBox="0 0 16 16"
                class="bi bi-check-lg text-primary">
                                    <path
                                        d="M12.736 3.97a.733.733 0 0 1 1.047 0c.286.289.29.756.01 1.05L7.88 12.01a.733.733 0 0 1-1.065.02L3.217 8.384a.757.757 0 0 1 0-1.06.733.733 0 0 1 1.047 0l3.052 3.093 5.4-6.425a.247.247 0 0 1 .02-.022Z"></path>
                                </svg></span><span>Nisl potenti ut auctor lobortis.</span></li>
          </ul>
        </div>
      </div>
      <div class="col">
        <div class="card mb-4">
          <div class="card-body text-center p-4">
            <h4 class="fw-bold card-subtitle">Enterprise</h4>
            <h4 class="display-5 fw-bold card-title">$70<span class="fs-4 fw-normal text-muted">/mo</span></h4>
            <p>Et lacinia fringilla massa.</p><a class="btn btn-dark d-block w-100" role="button" href="#">Button</a>
          </div>
        </div>
        <div class="bg-light border rounded border-light p-4">
          <ul class="list-unstyled">
            <li class="d-flex mb-2"><span class="bs-icon-xs bs-icon-rounded bs-icon-primary-light bs-icon me-2"><svg
                xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" viewBox="0 0 16 16"
                class="bi bi-check-lg text-primary">
                                    <path
                                        d="M12.736 3.97a.733.733 0 0 1 1.047 0c.286.289.29.756.01 1.05L7.88 12.01a.733.733 0 0 1-1.065.02L3.217 8.384a.757.757 0 0 1 0-1.06.733.733 0 0 1 1.047 0l3.052 3.093 5.4-6.425a.247.247 0 0 1 .02-.022Z"></path>
                                </svg></span><span>Lectus ut nibh quam, felis porttitor.</span></li>
            <li class="d-flex mb-2"><span class="bs-icon-xs bs-icon-rounded bs-icon-primary-light bs-icon me-2"><svg
                xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" viewBox="0 0 16 16"
                class="bi bi-check-lg text-primary">
                                    <path
                                        d="M12.736 3.97a.733.733 0 0 1 1.047 0c.286.289.29.756.01 1.05L7.88 12.01a.733.733 0 0 1-1.065.02L3.217 8.384a.757.757 0 0 1 0-1.06.733.733 0 0 1 1.047 0l3.052 3.093 5.4-6.425a.247.247 0 0 1 .02-.022Z"></path>
                                </svg></span><span>Ante nec venenatis etiam lacinia.</span></li>
            <li class="d-flex mb-2"><span class="bs-icon-xs bs-icon-rounded bs-icon-primary-light bs-icon me-2"><svg
                xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" viewBox="0 0 16 16"
                class="bi bi-check-lg text-primary">
                                    <path
                                        d="M12.736 3.97a.733.733 0 0 1 1.047 0c.286.289.29.756.01 1.05L7.88 12.01a.733.733 0 0 1-1.065.02L3.217 8.384a.757.757 0 0 1 0-1.06.733.733 0 0 1 1.047 0l3.052 3.093 5.4-6.425a.247.247 0 0 1 .02-.022Z"></path>
                                </svg></span><span>Porta suscipit netus ad ac.</span></li>
            <li class="d-flex mb-2"><span class="bs-icon-xs bs-icon-rounded bs-icon-primary-light bs-icon me-2"><svg
                xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" viewBox="0 0 16 16"
                class="bi bi-check-lg text-primary">
                                    <path
                                        d="M12.736 3.97a.733.733 0 0 1 1.047 0c.286.289.29.756.01 1.05L7.88 12.01a.733.733 0 0 1-1.065.02L3.217 8.384a.757.757 0 0 1 0-1.06.733.733 0 0 1 1.047 0l3.052 3.093 5.4-6.425a.247.247 0 0 1 .02-.022Z"></path>
                                </svg></span><span>Morbi praesent aptent integer at.</span></li>
            <li class="d-flex mb-2"><span class="bs-icon-xs bs-icon-rounded bs-icon-primary-light bs-icon me-2"><svg
                xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" viewBox="0 0 16 16"
                class="bi bi-check-lg text-primary">
                                    <path
                                        d="M12.736 3.97a.733.733 0 0 1 1.047 0c.286.289.29.756.01 1.05L7.88 12.01a.733.733 0 0 1-1.065.02L3.217 8.384a.757.757 0 0 1 0-1.06.733.733 0 0 1 1.047 0l3.052 3.093 5.4-6.425a.247.247 0 0 1 .02-.022Z"></path>
                                </svg></span><span>Nisl potenti ut auctor lobortis.</span></li>
          </ul>
        </div>
      </div>
    </div>
  </div>
  <footer class="text-center bg-dark">
    <div class="container text-white py-4 py-lg-5">
      <ul class="list-inline">
        <li class="list-inline-item me-4"><a class="link-light" href="#">Web design</a></li>
        <li class="list-inline-item me-4"><a class="link-light" href="#">Development</a></li>
        <li class="list-inline-item"><a class="link-light" href="#">Hosting</a></li>
      </ul>
      <ul class="list-inline">
        <li class="list-inline-item me-4">
          <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" viewBox="0 0 16 16"
               class="bi bi-facebook text-light">
            <path
                d="M16 8.049c0-4.446-3.582-8.05-8-8.05C3.58 0-.002 3.603-.002 8.05c0 4.017 2.926 7.347 6.75 7.951v-5.625h-2.03V8.05H6.75V6.275c0-2.017 1.195-3.131 3.022-3.131.876 0 1.791.157 1.791.157v1.98h-1.009c-.993 0-1.303.621-1.303 1.258v1.51h2.218l-.354 2.326H9.25V16c3.824-.604 6.75-3.934 6.75-7.951z"></path>
          </svg>
        </li>
        <li class="list-inline-item me-4">
          <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" viewBox="0 0 16 16"
               class="bi bi-twitter text-light">
            <path
                d="M5.026 15c6.038 0 9.341-5.003 9.341-9.334 0-.14 0-.282-.006-.422A6.685 6.685 0 0 0 16 3.542a6.658 6.658 0 0 1-1.889.518 3.301 3.301 0 0 0 1.447-1.817 6.533 6.533 0 0 1-2.087.793A3.286 3.286 0 0 0 7.875 6.03a9.325 9.325 0 0 1-6.767-3.429 3.289 3.289 0 0 0 1.018 4.382A3.323 3.323 0 0 1 .64 6.575v.045a3.288 3.288 0 0 0 2.632 3.218 3.203 3.203 0 0 1-.865.115 3.23 3.23 0 0 1-.614-.057 3.283 3.283 0 0 0 3.067 2.277A6.588 6.588 0 0 1 .78 13.58a6.32 6.32 0 0 1-.78-.045A9.344 9.344 0 0 0 5.026 15z"></path>
          </svg>
        </li>
        <li class="list-inline-item">
          <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" viewBox="0 0 16 16"
               class="bi bi-instagram text-light">
            <path
                d="M8 0C5.829 0 5.556.01 4.703.048 3.85.088 3.269.222 2.76.42a3.917 3.917 0 0 0-1.417.923A3.927 3.927 0 0 0 .42 2.76C.222 3.268.087 3.85.048 4.7.01 5.555 0 5.827 0 8.001c0 2.172.01 2.444.048 3.297.04.852.174 1.433.372 1.942.205.526.478.972.923 1.417.444.445.89.719 1.416.923.51.198 1.09.333 1.942.372C5.555 15.99 5.827 16 8 16s2.444-.01 3.298-.048c.851-.04 1.434-.174 1.943-.372a3.916 3.916 0 0 0 1.416-.923c.445-.445.718-.891.923-1.417.197-.509.332-1.09.372-1.942C15.99 10.445 16 10.173 16 8s-.01-2.445-.048-3.299c-.04-.851-.175-1.433-.372-1.941a3.926 3.926 0 0 0-.923-1.417A3.911 3.911 0 0 0 13.24.42c-.51-.198-1.092-.333-1.943-.372C10.443.01 10.172 0 7.998 0h.003zm-.717 1.442h.718c2.136 0 2.389.007 3.232.046.78.035 1.204.166 1.486.275.373.145.64.319.92.599.28.28.453.546.598.92.11.281.24.705.275 1.485.039.843.047 1.096.047 3.231s-.008 2.389-.047 3.232c-.035.78-.166 1.203-.275 1.485a2.47 2.47 0 0 1-.599.919c-.28.28-.546.453-.92.598-.28.11-.704.24-1.485.276-.843.038-1.096.047-3.232.047s-2.39-.009-3.233-.047c-.78-.036-1.203-.166-1.485-.276a2.478 2.478 0 0 1-.92-.598 2.48 2.48 0 0 1-.6-.92c-.109-.281-.24-.705-.275-1.485-.038-.843-.046-1.096-.046-3.233 0-2.136.008-2.388.046-3.231.036-.78.166-1.204.276-1.486.145-.373.319-.64.599-.92.28-.28.546-.453.92-.598.282-.11.705-.24 1.485-.276.738-.034 1.024-.044 2.515-.045v.002zm4.988 1.328a.96.96 0 1 0 0 1.92.96.96 0 0 0 0-1.92zm-4.27 1.122a4.109 4.109 0 1 0 0 8.217 4.109 4.109 0 0 0 0-8.217zm0 1.441a2.667 2.667 0 1 1 0 5.334 2.667 2.667 0 0 1 0-5.334z"></path>
          </svg>
        </li>
      </ul>
      <p class="text-muted mb-0">Copyright © 2022 Brand</p>
    </div>
  </footer>

  </body>

  </html>
</template>


<script>
import gql from 'graphql-tag'
import {provideApolloClient, useQuery, useResult} from "@vue/apollo-composable";
import {computed, watch} from "vue";
import ApolloClient, {InMemoryCache} from "apollo-boost";

import "../assets/homepage/bootstrap/css/bootstrap.min.css"
import "../assets/homepage/css/Navbar-Right-Links-Dark.css"
import "../assets/homepage/css/Pricing-Free-Paid.css"
import "../assets/homepage/css/styles.css"
import HeaderComp from "../components/HeaderComp.vue";

const CHARACTERS_QUERY = gql`
{
    allTips {
      heading
      description
      code
      dateCreated
      dateModified
      tags {
          name
      }
      urlHash
    }
}
`


export default {
  name: 'App',
  components: {
    HeaderComp
  },
  data() {
    return {
      search_tip: [],
      backend: '127.0.0.1:8000/',
      canClosed: true,
    }
  },
  setup() {
    const {result} = useQuery(CHARACTERS_QUERY);
    return {
      result,
    }
  },
  mounted() {
    let recaptchaScript = document.createElement('script')
    recaptchaScript.setAttribute('src', 'https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/js/bootstrap.bundle.min.js')
    document.head.appendChild(recaptchaScript)
    this.hideList()
  },
  methods: {
    hideList(event) {
      if (this.canClosed) {
        document.getElementById('tipslist').style.display = 'none'
      }
    },
    showList(event) {
      document.getElementById('tipslist').style.display = 'block'
    },
    onEnterSearch(event) {
      let search_val = event.target.value
      const cache = new InMemoryCache()
      const apolloClient = new ApolloClient({
        cache,
        uri: 'http://localhost:8000/blog/graphql',
      })
      provideApolloClient(apolloClient);
      if (event.target.value === '') {
        search_val = 'PineapplePen'
      }
      const SEARCH_QUERY = gql`
         query tipsByKeyword{
            tipsByKeyword(keyword: "${search_val}") {
            heading
            description
            code
            dateCreated
            dateModified
            tags {
              name
              icon
            }
            urlHash
          }
          }
        `
      const {result, loading, onError, onResult} = useQuery(SEARCH_QUERY)
      this.search_tip = computed(() => result.value?.tipsByKeyword ?? [])
    },
    GoToSearch() {
      let keywords = document.getElementById('search_input').value
      this.$router.push({
        name: 'search',
        params: {
          keywords: keywords,
        }
      });
    },
    GoToTip(tip) {
      this.$router.push({
        name: 'detail',
        params: {
          TipHash: tip,
        }
      });
    }
  }
}


</script>

<style>
#lib_search_input {
  width: -webkit-fill-available;
  max-width: 500px;
}

.search_tip_element {
  padding: 10px;
}

body, html {
  background-color: #f6f6f6 !important;
}

input[type="text"], textarea, button {
  outline: none;
  box-shadow: none !important;
}
</style>