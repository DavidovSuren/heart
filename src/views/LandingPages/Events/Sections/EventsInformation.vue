<script setup>
// example components
import DefaultInfoCard from "../../../../examples/cards/infoCards/DefaultInfoCard.vue";
import CenteredBlogCard from "../../../../examples/cards/blogCards/CenteredBlogCard.vue";
import WeekCalendar from '@/components/WeekCalendar.vue';

</script>
<template>
  <section class="py-7">
    <div class="container">
      <WeekCalendar/><hr>
      <div class="row align-items-center">
        <div class="col-lg-4 ms-auto mt-lg-0 mt-6 p-3">
          <CenteredBlogCard
            image="https://nashaplaneta.net/europe/russia/img_stavropol/dolphins.jpg"
            title="Представления в Кисловодском дельфинарии"
          />
        </div>
        <div class="col-lg-4 ms-auto mt-lg-0 mt-6 p-3">
          <CenteredBlogCard
            image="http://art-kislovodsk.ru/img/pages/about/002.jpg"
            title="Уникальная выставка картинной галереи «Art Room»"
          />
        </div>
        <div class="col-lg-4 ms-auto mt-lg-0 mt-6 p-3">
          <CenteredBlogCard
            image="https://trippo.ru/wp-content/uploads/2020/08/foto-2.jpg"
            title="Представления в Кисловодском дельфинарии"
          />
        </div>
        <div class="col-lg-4 ms-auto mt-lg-0 mt-6 p-3">
          <CenteredBlogCard
            image="https://trippo.ru/wp-content/uploads/2020/08/foto-2.jpg"
            title="Уникальная выставка картинной галереи «Art Room»"
          />
        </div>
        <div class="col-lg-4 ms-auto mt-lg-0 mt-6 p-3">
          <CenteredBlogCard
            image="https://trippo.ru/wp-content/uploads/2020/08/foto-2.jpg"
            title="Представления в Кисловодском дельфинарии"
          />
        </div>
        <div class="col-lg-4 ms-auto mt-lg-0 mt-6 p-3">
          <CenteredBlogCard
            image="https://trippo.ru/wp-content/uploads/2020/08/foto-2.jpg"
            title="Уникальная выставка картинной галереи «Art Room»"
          />
        </div>
        <div class="col-lg-4 ms-auto mt-lg-0 mt-6 p-3">
          <CenteredBlogCard
            image="https://trippo.ru/wp-content/uploads/2020/08/foto-2.jpg"
            title="Уникальная выставка картинной галереи «Art Room»"
          />
        </div>
        <div class="col-lg-4 ms-auto mt-lg-0 mt-6 p-3">
          <CenteredBlogCard
            image="https://trippo.ru/wp-content/uploads/2020/08/foto-2.jpg"
            title="Представления в Кисловодском дельфинарии"
          />
        </div>
        <div class="col-lg-4 ms-auto mt-lg-0 mt-6 p-3">
          <CenteredBlogCard
            image="https://trippo.ru/wp-content/uploads/2020/08/foto-2.jpg"
            title="Уникальная выставка картинной галереи «Art Room»"
          />
        </div>
      </div>
    </div>
  </section>
</template>