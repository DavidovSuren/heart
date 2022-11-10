<script setup>
// example components
import DefaultInfoCard from "../../../../examples/cards/infoCards/DefaultInfoCard.vue";
import CenteredBlogCard from "../../../../examples/cards/blogCards/CenteredBlogCard.vue";
</script>
<template>
  <section class="py-7">
    <div class="container">
      <div class="row align-items-center">
        <div class="col-lg-6">
          <div class="row justify-content-start">
            <DefaultInfoCard
              color="info"
              icon="view_day"
              title="Прокат велосипедов"
              description="Что может быть приятнее легкой прогулки по парку в солнечный денек? Только велопрогулка."
            />
            <DefaultInfoCard
              color="info"
              icon="view_day"
              title="Конные прогулки"
              description="Избавиться от стресса, почувствовать настоящий релакс и научится владеть собственным телом."
            />
          </div>
          <div class="row justify-content-start mt-4">
            <DefaultInfoCard
              color="info"
              icon="view_day"
              title="Картинг"
              description="Спортивный картинг является для одних первой ступенью в автоспорт, для других — дорогим, но увлекательным хобби."
            />
            <DefaultInfoCard
              color="info"
              icon="view_day"
              title="Прыжки с парашюта"
              description="Свободный полет с высоты +4000 метров длится 60 секунд."
            />
          </div>
        </div>
        <div class="col-lg-6 ms-auto mt-lg-0 mt-4">
          <CenteredBlogCard
            image="/src/assets/img/routesskis/СХЕМА Архитектурное наследие Нарзан.png"
          />
        </div>
      </div>
    </div>
  </section>
</template>
