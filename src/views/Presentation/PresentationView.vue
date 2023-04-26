<script setup>
import { onMounted, onUnmounted, ref } from "vue";

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
import vueMkHeader from "@/assets/img/GLAV/head.jpg";
import vueMkHeader1 from "@/assets/img/GLAV/kol.webp";
import vueMkHeader2 from "@/assets/img/GLAV/prich.jpg";
import vueMkHeader3 from "@/assets/img/GLAV/wow.jpeg";
//import vueMkHeader4 from "@/assets/img/GLAV/zrdav.jpg";
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

const header = ref(vueMkHeader);

const changeBack = (i) => {
  header.value = i;
};
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
    <div class="page-header min-vh-95" :style="`background-image: url(${header})`" loading="lazy">
      <div class="container flex-grow flex-shrink">
        <div class="row">
          <div class="col-lg-6 text-center mx-auto position-relative">
            <div id="intro">
              <h2 class="title">ГОРОД-КУРОРТ ФЕДЕРАЛЬНОГО ЗНАЧЕНИЯ</h2>

              <div class="scrollmenu slides">
                <div id="slide-accommodation"
                  class="slide navbar-expand-lg top-0 my-3 blur border-radius-lg z-index-3 py-2 shadow py-2 start-0 end-0 mx-3 mt-4"
                  @mouseleave="changeBack(vueMkHeader)">
                  <p></p>
                <p class="link">
                  <a href="https://www.russia-otdih.ru/" class="btn btn-blue btn-l text-dark"><span>
                      Проживание</span></a>
                </p>
                <p class="desc  ">
                    <a href="">40 <span>здравниц</span></a>
                  </p>
                </div>
                <div id="slide-fountain"
                  class="slide navbar-expand-lg top-0 my-3 blur border-radius-lg z-index-3 py-2 shadow py-2 start-0 end-0 mx-3 mt-4"
                  @mouseover="changeBack(vueMkHeader1)" @mouseleave="changeBack(vueMkHeader)">
                  <router-link to="/pages/landing-pages/points">

                  <p></p>
                  <p class="link">
                    <a href="" class="btn btn-blue btn-l text-dark"><span>Показать места</span></a>
                  </p>
                  <p class="desc">
                    <a href="">128 <span>интересных мест</span></a>
                  </p>
                </router-link>
                </div>

                <div id="slide-trip"
                  class="slide navbar-expand-lg top-0 my-3 blur border-radius-lg z-index-3 py-2 shadow py-2 start-0 end-0 mx-3 mt-4"
                  @mouseover="changeBack(vueMkHeader3)" @mouseleave="changeBack(vueMkHeader)">
                  <p></p>
                  <p class="link">
                    <a href="" class="btn btn-blue btn-l text-dark"><span>Показать экскурсии</span></a>
                  </p>
                  <p class="desc">
                    <a href="">17 <span>поездок</span></a>
                  </p>
                </div>
                <div id="slide-tenreason"
                  class="slide navbar-expand-lg top-0 my-3 blur border-radius-lg z-index-3 py-2 shadow py-2 start-0 end-0 mx-3 mt-4"
                  @mouseover="changeBack(vueMkHeader2)" @mouseleave="changeBack(vueMkHeader)">
                  <p></p>
                  <p class="link">
                    <a href="/pages/landing-pages/SPA" class="btn btn-blue btn-l text-dark"><span>Причины</span></a>
                  </p>
                  <p class="desc">
                    <a href="/pages/landing-pages/SPA">10<span>причин</span></a>
                  </p>
                </div>
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
            <MaterialSocialButton route="https://vk.com/heart_city_kissloveodsk" component="vk" color="instagram"
              label="vkontakte" />
            <MaterialSocialButton route="https://web.telegram.org/z/#" component="telegram" color="instagram"
              label="TELEGRAM" />
            <MaterialSocialButton route="" component="instagram" color="instagram" label="instagram" />
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
}

div.scrollmenu {
  background-color: #ffffff14;
  overflow-x: scroll;
  white-space: nowrap;
  position: absolute;
  left: -1em;
  right: -1em;
}

div.scrollmenu a {
  display: inline-block;
  color: white;
  text-align: center;
  padding: 0px 14px;
  text-decoration: none;
  color: black
}

.row-main {
  width: 10em;
  height: 10em;
  border: 3px solid rgb(155, 46, 180);
  border-radius: 50%;
  background: url(src/assets/img/bg4.webp);
  /* Путь к файлу с исходным  рисунком */
}

.slide {
  flex: 0 0 12em;
}

/*
.slides:after {
  content: '>';
  position: absolute;
  right: 3px;
  top: 72px;
  width: 26px;
  height: 25px;
  font-size: 1em;
  color: white;
  background: #ffffff14;
  border-radius: 50%;
  clear: both;

}
*/
.title {
  color: white;
  font-weight: 600;
  font-stretch: normal;
  font-size: 2.7em;
  font-family: Paris Typeface;
}
.page-header{ animation: changeBg 20s infinite}
@keyframes changeBg{
   0%,100%  {background-image: url("@/assets/img/GLAV/head.jpg");}
   25% {background-image: url("@/assets/img/GLAV/kol.webp");}
   50% {background-image: url("@/assets/img/GLAV/prich.jpg");}
   75% {background-image: url("@/assets/img/GLAV/wow.jpeg");}
}
@media (orientation: portrait) {
  h2 {
    font-size: 2em !important;
    opacity: 0.9;
    text-shadow: 1px 1px 2px rgba(255, 217, 0, 0.59), 0 0 0em black, 0 0 0.2em black;
  }
}
</style>
