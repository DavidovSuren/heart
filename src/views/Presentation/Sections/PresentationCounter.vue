<script setup>
import DefaultCounterCard from "../../../examples/cards/counterCards/DefaultCounterCard.vue";
</script>

<template>
  <section class="pt-4 pb-4" id="count-stats">
    <div class="container">
      <div class="row">
        <div class="col-lg-9 z-index-2 border-radius-xl mx-auto py-2">
          <div class="row">
            <div class="col-md-4 position-relative">
              <DefaultCounterCard
                color="success"
                title="Пользователей нам доверяют"
                :count="500"
                suffix="K+"
                :duration="3000"
                divider="vertical"
              />
            </div>
            <div class="col-md-4 position-relative">
              <DefaultCounterCard
                color="success"
                title="Мероприятий в год"
                description="Центр молодежи проводит сотни мероприятий."
                :count="100"
                suffix="+"
                :duration="3000"
                divider="vertical"
              />
            </div>
            <div class="col-md-4">
              <DefaultCounterCard
                color="success"
                title="Санатории"
                description="Санатории Кисловодска отлично подходят для лечения."
                :count="40"
                suffix="+"
                :duration="3000"
                @click="alert(1)"
                link="https://www.russia-otdih.ru/"
              />
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
