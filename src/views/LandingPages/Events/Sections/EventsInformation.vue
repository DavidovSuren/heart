<script setup>
// example components
/*
https://developer.wordpress.org/rest-api/using-the-rest-api/pagination/
*/
import { onMounted, ref } from "vue";
import WeekCalendar from "@/components/WeekCalendar.vue";
import MonthCalendar from "@/components/MonthCalendar.vue";
import ModalWindow from "../../../../layouts/sections/attention-catchers/modals/components/SimpleModal.vue";
import { dateEventStore } from "@/stores/pinia";
import { Carousel, Pagination, Slide, Navigation } from 'vue3-carousel';
import 'vue3-carousel/dist/carousel.css';

const nameMounth = [
  "января",
  "февраля",
  "марта",
  "апреля",
  "мая",
  "июня",
  "июля",
  "августа",
  "сентября",
  "октября",
  "ноября",
  "декабря",
];
const dataFilter = dateEventStore();
const mounth =  dataFilter?.mounth ; 
const date =  dataFilter?.day ; 
const Events = ref([]);
const getEvents = async () => {
  const url =
    "https://content.kissloveodsk.ru/wp-json/wp/v2/posts?categories=29&per_page=100";
  return fetch(url).then((response) => response.json());
};
onMounted(() => {
  getEvents().then((data) => {
    Events.value = data;
  });
  
});
function calculateBooksMessage() {
  let EventsList = Events.value.filter(
    (todo) =>
      todo.acf?.openday == dataFilter?.day &&
      todo.acf?.openmounth == dataFilter?.mounth
  );
  if (EventsList.length == 0) {
    EventsList = Events.value.filter(
      (todo) =>
        todo.acf?.openday > dataFilter?.day &&
        todo.acf?.openmounth >= 12
    );
  }
  console.log(dataFilter?.day, dataFilter.mounth, EventsList);
  return EventsList;
}

const places = [
  {
    title: "11",
    img: "https://vitest.dev/logo-shadow.svg",
    url: "http://1",
  },
  {
    title: "12",
    img: "https://vitest.dev/logo-shadow.svg",
    url: "http://1",
  },
  {
    title: "13",
    img: "https://vitest.dev/logo-shadow.svg",
    url: "http://1",
  },
  {
    title: "14",
    img: "https://vitest.dev/logo-shadow.svg",
    url: "http://1",
  },
  {
    title: "15",
    img: "https://vitest.dev/logo-shadow.svg"
  },
  {
    title: "16",
    img: "https://vitest.dev/logo-shadow.svg"
  },
  {
    title: "17",
    img: "https://vitest.dev/logo-shadow.svg"
  },
  {
    title: "18",
    img: "https://vitest.dev/logo-shadow.svg"
  },
];

</script>
<template>
  <Carousel :itemsToShow="3.95" :wrapAround="true" :transition="500">
    <Slide v-for="slide in places" :key="slide.title">
      <div class="carousel__item container_foto">
        <div class="container-container">
          <article class="text-left">
            <h2 style="color: #fff">{{ slide.title }}</h2>
          </article>
          <a :href="slide.url"><img :src="slide.img" /></a>
        </div>
      </div>
    </Slide>
    <template #addons>
      <navigation />
      <pagination />
    </template>
  </Carousel>
  <div class="container" style="margin-top: 50px">
    <MonthCalendar></MonthCalendar>
    <hr />
    <div class="row">
      <div
        v-for="Event in calculateBooksMessage()"
        :key="Event.id"
        class="col-lg-4 col-md-6 col-sm-12 container_foto"
        variant="gradient"
        color="success"
        data-bs-toggle="modal"
        :data-bs-target="`#m${Event.id}`"
      >
        <ModalWindow
          :id="`m${Event.id}`"
          :title="Event.title.rendered"
          :description="Event.excerpt.rendered"
          :img="Event.fimg_url"
          :acf="Event.acf"
          :openHour="Event.acf.openHour"
          :workPeriod="Event.acf.openPeriod"
        />
        <div class="container-container">
          <article class="text-left">
            <h2 v-html="Event.title.rendered"></h2>
            <h4 v-html="Event.excerpt.rendered"></h4>
          </article>
          <span class="text-right">
            {{ Event.acf.openday }} {{nameMounth[Event.acf.openmounth-1]}}
          </span>
          <img :src="Event.fimg_url" />
        </div>
      </div>
    </div>
  </div>
</template>
<style>
.carousel__slide {
  padding: 5px;
}

.carousel__viewport {
  perspective: 2000px;
}

.carousel__track {
  transform-style: preserve-3d;
}

.carousel__slide--sliding {
  transition: 0.5s;
}

.carousel__slide {
  opacity: 0.9;
  transform: rotateY(-20deg) scale(0.9);
}

.carousel__slide--active ~ .carousel__slide {
  transform: rotateY(20deg) scale(0.9);
}

.carousel__slide--prev {
  opacity: 1;
  transform: rotateY(-10deg) scale(0.95);
}

.carousel__slide--next {
  opacity: 1;
  transform: rotateY(10deg) scale(0.95);
}

.carousel__slide--active {
  opacity: 1;
  transform: rotateY(0) scale(1.1);
}
.container-container {
  margin: 10px;
  background-color: rgb(25, 40, 139);
}
.container_foto {
  padding: 0;
  overflow: hidden;
  position: relative;
  padding: 0 !important;
}

.container_foto article {
  position: absolute;
  bottom: 0;
  z-index: 1;
  -webkit-transition: all 0.5s ease;
  -moz-transition: all 0.5s ease;
  -o-transition: all 0.5s ease;
  -ms-transition: all 0.5s ease;
  transition: all 0.5s ease;
}

.text-right {
  display: flex;
  position: absolute;
  right: 0;
  top: 0;
  color:white;
  z-index: 100;
  background-color: rgba(36, 45, 81, 1);
  padding: 3px;
}

.container_foto h2 {
  color: #fff;
  font-weight: 800;
  font-size: 25px;
  border-bottom: #fff solid 1px;
  background: rgba(36, 45, 81, 0.613);
}

.container_foto h4 {
  font-weight: 300;
  color: #fff;
  font-size: 20px;
  background: rgba(36, 45, 81, 0.613);
}

.container_foto img {
  width: 100%;
  top: 0;
  left: 0;
  opacity: 1;
  -webkit-transition: all 1s ease;
  -moz-transition: all 1s ease;
  -o-transition: all 1s ease;
  -ms-transition: all 1s ease;
  transition: all 1s ease;
  display: block;
  height: 30vh;
  object-fit: cover;
}

.container_foto:hover {
  cursor: pointer;
}

.container_foto:hover img {
  opacity: 0.1;
  transform: scale(1.5);
}

.container_foto:hover article {
  transform: translate(2px, -69px);
  -webkit-transform: translate(2px, -69px);
  -moz-transform: translate(2px, -69px);
  -o-transform: translate(2px, -69px);
  -ms-transform: translate(2px, -69px);
}

.container_foto:hover .ver_mas {
  transform: translate(0px, 0px);
  -webkit-transform: translate(0px, 0px);
  -moz-transform: translate(0px, 0px);
  -o-transform: translate(0px, 0px);
  -ms-transform: translate(0px, 0px);
  opacity: 1;
}
</style>
