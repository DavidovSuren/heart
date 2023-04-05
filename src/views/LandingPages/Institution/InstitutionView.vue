<script setup>
import { onMounted, onUnmounted } from "vue";

//example components
import NavbarDefault from "../../../examples/navbars/NavbarDefault.vue";
import DefaultFooter from "../../../examples/footers/FooterDefault.vue";

//image
import bg3 from "@/assets/img/bannerchoco.jpeg";

//dep
import Typed from "typed.js";

//sections
import Information from "./Sections/InstitutionInformation.vue";
import InstitutionTeam from "./Sections/InstitutionTeam.vue";


const body = document.getElementsByTagName("body")[0];
//hooks
onMounted(() => {
  body.classList.add("institution");
  body.classList.add("bg-gray-200");

  if (document.getElementById("typed")) {
    // eslint-disable-next-line no-unused-vars
    var typed = new Typed("#typed", {
      stringsElement: "#typed-strings",
      typeSpeed: 90,
      backSpeed: 90,
      backDelay: 200,
      startDelay: 500,
      loop: true,
    });
  }
});

onUnmounted(() => {
  body.classList.remove("institution");
  body.classList.remove("bg-gray-200");
});
</script>
<template>
  <div class="container position-sticky z-index-sticky top-0">
    <div class="row">
      <div class="col-12">
        <NavbarDefault :sticky="true" />
      </div>
    </div>
  </div>
  <header class="bg-gradient-dark">
    <div
      class="page-header min-vh-85"
      :style="{ backgroundImage: `url(${bg3})` }"
    >
      <span class="mask bg-gradient-dark opacity-2"></span>
      <div class="container">
        <div class="row justify-content-center">
          <div class="col-lg-12 text-center mx-auto my-auto">
            <h1 class="text-white">
             ЛУЧШИЕ ЗАВЕДЕНИЯ КИСЛОВОДСКА<span class="text-white" id="typed"></span>
            </h1>
            <div id="typed-strings">
              <h1></h1>
            </div>
            </div>
          </div>
        </div>
      </div>
  </header>
  <div class="card card-body shadow-xl mx-3 mx-md-4 mt-n6">
    <Information />
    <AboutTeam />
    <Featuring />
    <Newsletter />
  </div>
  <DefaultFooter />
</template>
