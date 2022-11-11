<script setup>
import { onMounted, onUnmounted } from "vue";

import ExcursionsModal from "../../layouts/sections/attention-catchers/modals/components/ExcursionsModal.vue";

//example components
import NavbarDefault from "../..//examples/navbars/NavbarDefault.vue";
import DefaultFooter from "../../examples/footers/FooterDefault.vue";
import Header from "../../examples/Header.vue";
import FilledInfoCard from "../../examples/cards/infoCards/FilledInfoCard.vue";

//Vue Material Kit 2 components
import MaterialSocialButton from "@/components/MaterialSocialButton.vue";

// sections
import PresentationCounter from "./Sections/PresentationCounter.vue";
import PresentationPages from "./Sections/PresentationPages.vue";
import PresentationExample from "./Sections/PresentationExample.vue";
import data from "./Sections/Data/designBlocksData";
import BuiltByDevelopers from "./Components/BuiltByDevelopers.vue";
import PresentationTestimonials from "./Sections/PresentationTestimonials.vue";
import PresentationInformation from "./Sections/PresentationInformation.vue";

//images
import vueMkHeader from "@/assets/img/vue-mk-header.jpg";
import wavesWhite from "@/assets/img/waves-white.svg";
import logoBootstrap from "@/assets/img/logos/bootstrap5.jpg";
import logoTailwind from "@/assets/img/logos/icon-tailwind.jpg";
import logoVue from "@/assets/img/logo-ct-dark.png";
import logoAngular from "@/assets/img/logos/angular.jpg";
import logoReact from "@/assets/img/logos/react.jpg";
import logoSketch from "@/assets/img/logos/sketch.jpg";

//hooks
const body = document.getElementsByTagName("body")[0];
onMounted(() => {
  body.classList.add("presentation-page");
  body.classList.add("bg-gray-200");
});
onUnmounted(() => {
  body.classList.remove("presentation-page");
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
  <Header>
    <div
      class="page-header min-vh-75"
      :style="`background-image: url(${vueMkHeader})`"
      loading="lazy"
    >
      <div class="container">
        <div class="row">
          <div class="col-lg-7 text-center mx-auto position-relative">
            <h1
              class="text-white pt-3 mt-n5 me-2"
              :style="{ display: 'inline-block ' }"
            >
              КИСЛОВОДСК  
            </h1>
            <p class="lead text-white px-5 mt-3" :style="{ fontWeight: '500' }">
              Курортный город 
              </p>
          </div>
        </div>
      </div>
    </div>
  </Header>
  <ExcursionsModal />

  <!-- <section class="front-page-6" style="text-align: center;">
          <h3 class="sec-h">Партнёры</h3>
          <a href="https://artclip.ru/"><img width="100" height="100" src="images/L9bVYfpPTQuj.png"
              style="margin-right: 30px;" /></a>
          <a href="https://www.russia-otdih.ru/"><img width="100" height="100" src="images/part.jpeg" /></a>
        </section>-->
  <div class="card card-body blur shadow-blur mx-3 mx-md-4 mt-n6">
    <PresentationCounter />
    <PresentationInformation />
    <PresentationExample :data="data" />
    <PresentationPages />
    <BuiltByDevelopers />
    <PresentationTestimonials />
    <div class="container">
      <div class="row">
        <div class="d-flex flex-column w-100 text-center p-5 mb-8">
          <h3>ПАРТНЁРЫ</h3>
          <div class="d-flex justify-content-center mt-3 flex-wrap">
            <a
              href="https://artclip.ru"
              data-bs-toggle="tooltip"
              data-bs-placement="bottom"
              title="ВИДЕО И ФОТОСЪЕМКА НА КМВ"
            >
              <img
                :src="logoBootstrap"
                alt="title"
                loading="lazy"
                :style="{ height: '90px' }"
              />
            </a>
            <a
              class="opacity-5 ms-3"
              href="https://www.russia-otdih.ru/"
              data-bs-toggle="tooltip"
              data-bs-placement="bottom"
              title="ТУРИСТИЧЕСКОЕ АГЕНСТВО"
            >
              <img
                :src="logoTailwind"
                alt="title"
                loading="lazy"
                :style="{ height: '90px' }"
              />
            </a>
          </div>
        </div>
      </div>
    </div>
    <div class="py-1">
      <div class="container">
        <div class="row">
          <div class="col-lg-5 ms-auto">
            <h4 class="mb-1">Спасибо за Вашу поддержку!</h4>
            <p class="lead mb-0">СОЦИАЛЬНЫЕ СЕТИ</p>
          </div>
          <div class="col-lg-5 me-lg-auto my-lg-auto text-lg-end mt-5">
            <MaterialSocialButton
              route="https://vk.com/heart_city_kissloveodsk"
              component="vk"
              color="instagram"
              label="vkontakte"
            />
            <MaterialSocialButton
              route="https://web.telegram.org/z/#DavydoV_Sss"
              component="telegram"
              color="instagram"
              label="TELEGRAM"
            />
            <MaterialSocialButton
              route=""
              component="instagram"
              color="instagram"
              label="instagram"
            />
          </div>
        </div>
      </div>
    </div>
  </div>
  <DefaultFooter />
</template>
