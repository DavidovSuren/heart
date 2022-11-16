<script setup>
import RotatingCard from "../../../examples/cards/rotatingCards/RotatingCard.vue";
import RotatingCardFront from "../../../examples/cards/rotatingCards/RotatingCardFront.vue";
import RotatingCardBack from "../../../examples/cards/rotatingCards/RotatingCardBack.vue";
import DefaultInfoCard from "../../../examples/cards/infoCards/DefaultInfoCard.vue";
import imageSrc from "@/assets/img/Gorod.jpeg"

</script>
<template>
  <section class="my-5 py-5">
    <div class="container">
      <div class="row align-items-center">
        <div class="col-lg-4 ms-auto me-auto p-lg-4 mt-lg-0 mt-4">
          <RotatingCard>
            <RotatingCardFront
              image="https://images.unsplash.com/photo-1569683795645-b62e50fbf103?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=987&q=80"
              icon="touch_app"
              title="Афиша <br />"
            />

            <RotatingCardBack
              :image="imageSrc"
              title="Лучшие события"
              :action="[
                {
                  route: '/pages/landing-pages/Events',
                  label: 'Перейти',
                },
              ]"
            />
          </RotatingCard>
        </div>
        <div class="col-lg-6 ms-auto">
          <div class="row justify-content-start">
            <DefaultInfoCard
              icon="content_copy"
              title="Санатории"
              description="Санатории Кисловодска отлично подходят для лечения."
              link="https://www.russia-otdih.ru/"
            />
            <DefaultInfoCard
              icon="flip_to_front"
              title="Заведения"
              description="Лучшие заведения города-курорта Кисловодска."
              link="/pages/landing-pages/Institution"
            />
          </div>
          <div class="row justify-content-start mt-5">
            <DefaultInfoCard
              class="mt-3"
              icon="flip_to_front"
              title="СПА"
              description="Восстановительная медицина."
              link="/pages/landing-pages/SPA"
            />
            <DefaultInfoCard
              class="mt-3"
              icon="content_copy"
              title="Новости"
              description="КИСЛОВОДСКА."
                  link="https://ria.ru/location_Kislovodsk/"
            />
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

