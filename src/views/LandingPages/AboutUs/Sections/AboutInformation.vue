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
              icon="public"
              title="Прокат велосипедов"
              description="Что может быть приятнее легкой прогулки по парку в солнечный денек? Только велопрогулка."
            />
            <DefaultInfoCard
              color="info"
              icon="payments"
              title="Конные прогулки"
              description="Избавиться от стресса, почувствовать настоящий релакс и научится владеть собственным телом."
            />
          </div>
          <div class="row justify-content-start mt-4">
            <DefaultInfoCard
              color="info"
              icon="apps"
              title="Картинг"
              description="Спортивный картинг является для одних первой ступенью в автоспорт, для других — дорогим, но увлекательным хобби."
            />
            <DefaultInfoCard
              color="info"
              icon="3p"
              title="Прыжки с парашюта"
              description="Свободный полет с высоты +4000 метров длится 60 секунд."
            />
          </div>
        </div>
        <div class="col-lg-4 ms-auto mt-lg-0 mt-6">
          <CenteredBlogCard
            image="https://trippo.ru/wp-content/uploads/2020/08/foto-2.jpg"
            title="Достопримечательности Кисловодска"
          />
        </div>
      </div>
    </div>
  </section>
</template>
