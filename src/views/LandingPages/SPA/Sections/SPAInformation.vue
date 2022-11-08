<script setup>
// example components
import DefaultInfoCard from "../../../../examples/cards/infoCards/DefaultInfoCard.vue";
import CenteredBlogCard from "../../../../examples/cards/blogCards/CenteredBlogCard.vue";
</script>
<template>
  <div class="container" style="margin-top: 50px">
   <div class="row">
     <div class="col-4 container_foto">
       <div class="container-container">
         <article class="text-left">
           <h2>Квалификационный шахматный фестиваль </h2>
           <h4>«Золотая осень»</h4>
         </article>
         <img src="https://img-aws.ehowcdn.com/400x400/ds-img.studiod.com/Half_Dome_from_Glacier_Point0_1.jpg" />
       </div>
     </div>
     <div class="col-4 container_foto">
       <div class="container-container">
         <article class="text-left">
           <h2>«Школа ИЗО для взрослых»</h2>
           <h4>мастер-класс в технике Акварель</h4>
         </article>
         <img src="https://img-aws.ehowcdn.com/400x400/ds-img.studiod.com/Half_Dome_from_Glacier_Point0_1.jpg" />
       </div>
     </div>
     <div class="col-4 container_foto">
       <div class="container-container">
         <article class="text-left">
           <h2>Мастер-классы по правополушарному рисованию</h2>
         </article>
         <img src="https://img-aws.ehowcdn.com/400x400/ds-img.studiod.com/Half_Dome_from_Glacier_Point0_1.jpg" />
       </div>
     </div>
   </div>
   <div class="row">
     <div class="col-4 container_foto">
       <div class="container-container">
         <article class="text-left">
           <h2>Выполнение нормативов ВФСК ГТО</h2>
           <h4>учащихся учреждений образования (IV-VI
ступени) и все желающие</h4>
         </article>
         <img src="https://img-aws.ehowcdn.com/400x400/ds-img.studiod.com/Half_Dome_from_Glacier_Point0_1.jpg" />
       </div>
     </div>
     <div class="col-4 container_foto">
       <div class="container-container">
         <article class="text-left">
           <h2>Сказочный час</h2>
           <h4>«Со сказками Маршака поведешься - ума наберешься»</h4>
         </article>
         <img src="https://img-aws.ehowcdn.com/400x400/ds-img.studiod.com/Half_Dome_from_Glacier_Point0_1.jpg" />
       </div>
     </div>
     <div class="col-4 container_foto">
       <div class="container-container">
         <article class="text-left">
           <h2>Квалификационный шахматный фестиваль <br />«Золотая осень»</h2>
           <h4>среди детей
приуроченный ко Дню народного единства</h4>
         </article>
         <img src="https://img-aws.ehowcdn.com/400x400/ds-img.studiod.com/Half_Dome_from_Glacier_Point0_1.jpg" />
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
 -webkit-transition: all 4s ease;
 -moz-transition: all 4s ease;
 -o-transition: all 4s ease;
 -ms-transition: all 4s ease;
 transition: all 4s ease;
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
