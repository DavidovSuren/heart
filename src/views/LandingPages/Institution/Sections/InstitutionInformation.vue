<script setup>
// example components
import ModalWindow from "../../../../layouts/sections/attention-catchers/modals/components/SimpleModal.vue";
const InstitutionList = [
  {
    id: "m1",
    title: "Кафе Шоколад",
    description: "«Золотая осень»",
    img: "https://content.kissloveodsk.ru/wp-content/uploads/2022/09/photo1662493588.jpeg",
  },
  {
    id: "m2",
    title: "Школа ИЗО для взрослых»",
    description: "мастер-класс в технике Акварель",
    img: "https://img-aws.ehowcdn.com/400x400/ds-img.studiod.com/Half_Dome_from_Glacier_Point0_1.jpg",
  },
  {
    id: "m3",
    title: "ГТО",
    description: "Выполнение нормативов ВФСК ГТО",
    img: "https://gradkostroma.ru/i/news/gto18.jpg",
  },
];
</script>
<template>
  <div class="container" style="margin-top: 50px">
    <div class="row">
      <div
        v-for="Institution in InstitutionList"
        :key="Institution.id"
        class="col-4 container_foto"
        variant="gradient"
        color="success"
        data-bs-toggle="modal"
        :data-bs-target="`#${Institution.id}`"
      >
        <ModalWindow
          :id="Institution.id"
          :title="Institution.title"
          :description="Institution.description"
          :img="Institution.img"
        />
        <div class="container-container">
          <article class="text-left">
            <h2>{{ Institution.title }}</h2>
            <h4>{{ Institution.description }}</h4>
          </article>
          <img :src="Institution.img" />
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
}

.container_foto h4 {
  font-weight: 300;
  color: #fff;
  font-size: 20px;
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
