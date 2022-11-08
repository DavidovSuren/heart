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
        <div class="col-lg-4 ms-auto mt-lg-0 mt-6 p-4">
          <CenteredBlogCard
            image="https://www.m24.ru/b/d/nBkSUhL2hFYun8ayJb6BvMKnxdDs95C-yyqYy7jLs2KQeXqLBmmcmzZh59JUtRPBsdaJqSfJd54qEr7t1mNwKSGK7WY=j7cw0N1gK8ksR9bJT3WDIA.jpg"
            title="Квалификационный шахматный фестиваль"
          />
        </div>
        <div class="col-lg-4 ms-auto mt-lg-0 mt-6 p-4">
          <CenteredBlogCard
            image="https://prorisunok.ru/source/img_index/blocky/orgk.jpg"
            title="«Школа ИЗО для взрослых»"
          />
        </div>
        <div class="col-lg-4 ms-auto mt-lg-0 mt-6 p-4">
          <CenteredBlogCard
            image="https://media.1777.ru/images/images_processing/578/5788922556184791.jpeg"
            title="Мастер-классы по правополушарному рисованию"
          />
        </div>
        <div class="col-lg-4 ms-auto mt-lg-0 mt-6 p-4">
          <CenteredBlogCard
            image="https://trippo.ru/wp-content/uploads/2020/08/foto-2.jpg"
            title="Уникальная выставка картинной галереи «Art Room»"
          />
        </div>
        <div class="col-lg-4 ms-auto mt-lg-0 mt-6 p-4">
          <CenteredBlogCard
            image="https://trippo.ru/wp-content/uploads/2020/08/foto-2.jpg"
            title="Представления в Кисловодском дельфинарии"
          />
        </div>
        <div class="col-lg-4 ms-auto mt-lg-0 mt-6 p-4">
          <CenteredBlogCard
            image="https://trippo.ru/wp-content/uploads/2020/08/foto-2.jpg"
            title="Уникальная выставка картинной галереи «Art Room»"
          />
        </div>
        <div class="col-lg-4 ms-auto mt-lg-0 mt-6 p-4">
          <CenteredBlogCard
            image="https://trippo.ru/wp-content/uploads/2020/08/foto-2.jpg"
            title="Уникальная выставка картинной галереи «Art Room»"
          />
        </div>
        <div class="col-lg-4 ms-auto mt-lg-0 mt-6 p-4">
          <CenteredBlogCard
            image="https://trippo.ru/wp-content/uploads/2020/08/foto-2.jpg"
            title="Представления в Кисловодском дельфинарии"
          />
        </div>
        <div class="col-lg-4 ms-auto mt-lg-0 mt-6 p-4">
          <CenteredBlogCard
            image="https://trippo.ru/wp-content/uploads/2020/08/foto-2.jpg"
            title="Уникальная выставка картинной галереи «Art Room»"
          />
        </div>
      </div>
    </div>
  </section>
</template>