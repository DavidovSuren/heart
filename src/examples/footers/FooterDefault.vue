<script setup>
import ExcursionsModal from "../../layouts/sections/attention-catchers/modals/components/ExcursionsModal.vue";

defineProps({
  brand: {
    type: Object,
    name: String,
    route: "",
    default: () => ({
      name: "Сердце города ",
      route: "/",
    }),
  },
  menus: {
    type: Array,
    name: String,
    items: {
      type: Array,
      name: String,
      href: String,
    },
    default: () => [
      {
        name: "Мы используем Cookie",
        items: [

          {
            name: "",
          },
        ],
      },
      {
        name: "Контакты",
        items: [
          {
            name: "+7 (928) 007 5243 ",
          },
          {
            name: "Gmail",
            href: "",
          },
        ],
      },
      {
        name: "ФЗ",
        items: [
          {
            name: "Политика конфиденциальности",
            href: "/pages/landing-pages/POL",
          },
        ],
      },
    ],
  },
});
</script>
<template>
  <footer class="footer pt-5 mt-5">
    <div class="container">
      <div class="row">
        <div class="col-md-3 mb-4 ms-auto">
          <div>
            <h6 class="font-weight-bolder mb-4">{{ brand.name }}</h6>
          </div>
          <div>
            <ul class="d-flex flex-row ms-n3 nav">
              <li
                class="nav-item"
                v-for="{ icon, link } of socials"
                :key="link"
              >
                <a
                  class="nav-link pe-1"
                  :href="link"
                  target="_blank"
                  v-html="icon"
                >
                </a>
              </li>
            </ul>
          </div>
        </div>
        <div
          class="col-md-3 col-sm-6 col-6 mb-4"
          v-for="{ name, items } of menus"
          :key="name"
        >
          <h6 class="text-md">{{ name }}</h6>
          <ul class="flex-column ms-n3 nav">
            <li class="nav-item" v-for="item of items" :key="item.name">
              <a class="nav-link" :href="item.href" target="_blank">
                {{ item.name }}
              </a>
            </li>
          </ul>
        </div>

        <div class="col-12">
          <div class="text-center">
            <p class="text-dark my-4 text-sm font-weight-normal">
              Все права защищены. Авторские права ©
              {{ new Date().getFullYear() }}
              Сердце города КИСЛОВОДСКА
            </p>
          </div>
        </div>
      </div>
    </div>
    <ExcursionsModal />
  </footer>
</template>
