<script setup>
import { onMounted, ref } from "vue";
import ModalWindow from "../../../../layouts/sections/attention-catchers/modals/components/SimpleModal.vue";
const Institutions = ref([]);
const BaseUrl = `https://кисловодск.онлайн/rest`;
const id = "";
const itemUrl = `${BaseUrl}/api/catering/${id}`;

const getInstitutions = async (c) => {
  let cat = "";
  if (c === "rest") {
    cat = "r";
  } else if (c === "cafe") {
    cat = "c";
  } else {
    cat = "";
  }
const url = `${BaseUrl}/api/catering/?format=json&category=${cat}`;
//const url = `http://127.0.0.1:8000/api/catering/?format=json&category=${cat}`;

  return fetch(url).then((response) => response.json());
};
onMounted(() => {
  getInstitutions("all").then((data) => {
    Institutions.value = data;
  });
});

const counter = async (id) => {
  fetch(itemUrl+id);
 };
const get = async (c) => {
  getInstitutions(c).then((data) => {
    Institutions.value = data;
  });
};


function parseSrc(rendered) {
  let listArr = [];
  rendered
    .split('alt="')
    .forEach((element) => listArr.push(element.split('src="')[1]));
  return listArr;
}
</script>
<template>
  <div class="row">
    <div class="col-6 col-sm-6 col-md-6 col-lg-6" style="text-align: right">
      <button type="button" class="btn btn-success btn-lg" @click="get('rest')">
        РЕСТОРАНЫ
      </button>
    </div>
    <div class="col-6 col-sm-6 col-md-6 col-lg-6">
      <button type="button" class="btn btn-success btn-lg" @click="get('cafe')">
        КАФЕ
      </button>
    </div>
  </div>
  <div class="container" style="margin-top: 20px">
    <div class="row">
      <div
        v-for="Institution in Institutions"
        :key="Institution.id"
        class="col-lg-4 col-md-6 col-sm-12"
        variant="gradient"
        color="success"
        data-bs-toggle="modal"
        :data-bs-target="`#m${Institution.id}`"
      >
        <ModalWindow
          :id="`m${Institution.id}`"
          :title="Institution.title"
          :description="Institution.description"
          :img="Institution.img"
          :rating="Institution.rating"
          :content="Institution.description"
          :card_content="Institution.description"
          :whatsapp="Institution.whatsapp"
          :openHour="Institution.openHour"
          :video = "Institution.video"
          :menu = "Institution.menu"
          :workPeriod="Institution?.workPeriod"
          :phone="Institution?.phone"
          :address="Institution?.address"
          :gallery="Institution?.gallery"
          :photos="Institution?.photos"
        />
        <div class="container-container"         @click="counter(Institution.id)">
          <article class="text-left">
            <h2 v-html="Institution.title"></h2>
                    
            <h4><i class="large material-icons me-2 m-1 pb-1 " aria-hidden="true">remove_red_eye</i>{{ Institution.count}}</h4> 
          </article>
          <img :src="Institution.img" />
          
        </div>
      </div>
    </div>
  </div>
</template>
<style scoped>
.container-container {
  margin: 10px;
  background-color: rgb(25, 40, 139);
}
.container-container {
  padding: 0;
  overflow: hidden;
  position: relative;
  padding: 0 !important;
}

.container-container article {
  position: absolute;
  bottom: 0;
  z-index: 1;
  -webkit-transition: all 0.5s ease;
  -moz-transition: all 0.5s ease;
  -o-transition: all 0.5s ease;
  -ms-transition: all 0.5s ease;
  transition: all 0.5s ease;
}

.container-container h2 {
  color: #fff;
  font-weight: 800;
  font-size: 25px;
  border-bottom: #fff solid 1px;
  background: rgba(36, 45, 81, 0.613);
}

.container-container h4 {
  font-weight: 300;
  color: #fff;
  font-size: 20px;
  background: rgba(36, 45, 81, 0.613);
}

.container-container img {
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

.container-container:hover {
  cursor: pointer;
}

.container-container:hover img {
  opacity: 0.1;
  transform: scale(1.5);
}

.container-container:hover article {
  transform: translate(2px, -69px);
  -webkit-transform: translate(2px, -69px);
  -moz-transform: translate(2px, -69px);
  -o-transform: translate(2px, -69px);
  -ms-transform: translate(2px, -69px);
}
</style>
