<script setup>
import { onMounted, onUnmounted } from "vue";

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
            <div id="intro">
            <h2 class="title">уникальный курортный город  </h2>
            <div class="slides">
                <div id="slide-accommodation" class="slide">
                    <div class="row-main">
                        <p></p>
                        <p class="link">
                            <a href="/ru/prozhivanie" class="btn btn-blue btn-l"><span>Изобразить проживание</span></a>
                        </p>
                        <p class="desc"><a href="/ru/prozhivanie">151 <span>здравниц</span></a></p>
                    </div>
                </div>
               <ul> <div id="slide-fountain" class="slide">
                    <div class="row-main">
                        <p></p>
                        <p class="link">
                            <a href="/ru/interesnye-punkty" class="btn btn-blue btn-l"><span>Показать места</span></a>
                        </p>
                        <p class="desc"><a href="/ru/interesnye-punkty">128 <span>интересных мест</span></a></p>
                    </div>
                </div>
              </ul>
                <ul><div id="slide-trip" class="slide">
                    <div class="row-main">
                        <p></p>
                        <p class="link">
                            <a href="/ru/ekskursii-v-okresnosti" class="btn btn-blue btn-l"><span>Показать экскурсии</span></a>
                        </p>
                        <p class="desc"><a href="/ru/ekskursii-v-okresnosti">17 <span>поездок</span></a></p>
                    </div>
                </div>
              </ul>
                <ul><div id="slide-tenreason" class="slide">
                    <div class="row-main">
                        <p></p>
                        <p class="link">
                            <a href="/pages/landing-pages/SPA" class="btn btn-blue btn-l"><span>Изобразить причины</span></a>
                        </p>
                        <p class="desc"><a href="/pages/landing-pages/SPA">10<span>причин</span></a></p>
                    </div>
                </div>
          </ul>
            </div>
         
        </div>
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
              route="https://web.telegram.org/z/#"
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
<style>
.slides {
  display: flex;
  width: 10em;
  height: 10em;
  border: 3px solid rgb(155, 46, 180);
  border-radius: 50%;

}
.row-main {
  width: 10em;
  height: 10em;
  border: 3px solid rgb(155, 46, 180);
  border-radius: 50%;
  background: url(src/assets/img/bg4.webp); /* Путь к файлу с исходным  рисунком */
}

</style>