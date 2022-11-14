<script setup>
import ExampleCard from "../Components/ExampleCard.vue";
import MaterialBadge from "../../../components/MaterialBadge.vue";

// images
import imgSigninCover from "@/assets/img/signin-cover.png";
</script>
<template>
  <section class="py-1">
    <div class="container">
      <div class="row">
        <div class="row text-center my-sm-1 mt-1">
            <h2 class="">ТУРИЗМ
            </h2>
          </div>
        </div>
      </div>
    <div class="container mt-3">
      <div class="row">
        <div class="col-md-6">
              <ExampleCard
                class="shadow-lg"
                image="src/assets/img/about-us4.jpg"
                route="about"
              />
        </div>
        <div class="col-md-6 mt-md-2 mt-4">
          <div class="position-sticky" style="top: 100px !important">
            <h4>
              Крупнейший в Европе городской парк. Парк делится на три части. Нижний парк начинается от Нарзанной галереи. От Сосновой горки и Площадки роз до Храма воздуха – средний парк. От Храма воздуха начинается верхний парк.
            </h4>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
