<script setup>
import { onMounted, ref } from "vue";
import ModalWindow from "../../../../layouts/sections/attention-catchers/modals/components/SimpleModal.vue";
const About = ref([]);
const getAbout = async () => {
  return fetch(
    "https://content.kissloveodsk.ru/wp-json/wp/v2/posts?categories=46&per_page=50"
  ).then((response) => response.json());
};
onMounted(() => {
  getAbout().then((data) => {
    About.value = data;
  });
});
</script>
<template>
  <div class="container" style="margin-top: 20px">
    <div class="row">
      <div
        v-for="About in About"
        :key="About.id"
        class="col-lg-4 col-md-6 col-sm-12 container_foto"
        variant="gradient"
        color="success"
        data-bs-toggle="modal"
        :data-bs-target="`#m${About.id}`"
      >
        <ModalWindow
          :id="`m${About.id}`"
          :title="About.title.rendered"
          :description="About.excerpt.rendered"
          :img="About.fimg_url"
          :acf="About.acf"
        />
        <div class="container-container">
          <article class="text-left">
            <h2 v-html="About.title.rendered"></h2>
            <h4 v-html="About.excerpt.rendered"></h4>
          </article>
          <img :src="About.fimg_url" />
        </div>
      </div>
    </div>
  </div>
</template>
<style>
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
