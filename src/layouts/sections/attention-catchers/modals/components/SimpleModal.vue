<script setup>
import MaterialButton from "@/components/MaterialButton.vue";
import MaterialBadge from "@/components/MaterialBadge.vue";

defineProps({
  id: {
    type: String,
  },
  title: {
    type: String,
  },
  description: {
    type: String,
  },
  img: {
    type: String,
  },
  content: {
    type: Object,
  },
  acf: {
    type: Object,
  },
});
</script>
<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-3 col-6 mx-auto">
        <!-- Modal -->
        <div
          class="modal fade"
          :id="id"
          tabindex="-1"
          aria-labelledby="exampleModalLabel"
          aria-hidden="true"
        >
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-body card">
                <div class="row">
                  <div
                    class="avatar-container"
                    :style="`background-image: url(${img});`"
                  ></div>
                  <div class="details-container">
                    <div class="content">
                      <h3 v-html="title"></h3>
                      <vue3-star-ratings
                        starSize="32"
                        showControl="false"
                        disableClick="true"
                        v-model="acf.рейтинг"
                      />
                      <p v-html="acf.card_content"></p>

                      <!-- {{ acf.фото }}
                      { acf.openHour }}
                      {{ acf.openday }}
                      {{ acf.openminute }}
                      {{ acf.openmounth }}-->

                      {{ acf.whatsapp }}

                      <div
                        class="btn-group btn-group-md"
                        role="group"
                        aria-label="Basic example"
                      ></div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="modal-footer justify-content-between">
                <MaterialButton
                  variant="gradient"
                  color="dark"
                  data-bs-dismiss="modal"
                >
                  Закрыть
                </MaterialButton>

                <MaterialButton
                  variant="contained"
                  color="success"
                  v-if="acf.видео"
                >
                  <a :href="`${acf.видео}`" target="_blank"> Видео </a>
                </MaterialButton>
                <a v-if="acf.меню" :href="`${acf.меню}`" target="_blank">
                  <img
                    src="@/assets/img/Меню.png"
                    style="width: 80px; height: 80px"
                /></a>
                <MaterialButton
                  variant="outline"
                  color="info"
                  class="w-auto me-2"
                  v-if="acf.адрес"
                >
                  <a :href="`${acf.адрес}`" target="_blank">
                    {{ acf.адрес }}
                  </a>
                </MaterialButton>
                <MaterialButton
                  variant="outline"
                  color="info"
                  class="w-auto me-2"
                  v-if="acf.телефон"
                >
                  <a :href="`tel:${acf.телефон}`">{{ acf.телефон }}</a>
                </MaterialButton>
              </div>

              <div class="modal-footer justify-content-between">
                <img
                  v-for="src in content"
                  :src="src"
                  :alt="src"
                  :key="src"
                  style="width: 100%"
                />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<style scoped>
.modal-body img {
  width: 100%;
  margin: auto;
}

.star-rating {
  font-size: 0;
}

.star-rating__wrap {
  display: inline-block;
  font-size: 1rem;
}

.star-rating__wrap:after {
  content: "";
  display: table;
  clear: both;
}

.star-rating__ico {
  float: right;
  padding-left: 2px;
  cursor: pointer;
  color: #ffb300;
}

.star-rating__ico:last-child {
  padding-left: 0;
}

.star-rating__input {
  display: none;
}

.star-rating__ico:hover:before,
.star-rating__ico:hover ~ .star-rating__ico:before,
.star-rating__input:checked ~ .star-rating__ico:before {
  content: "f005";
}

.card {
  background-color: white;
  padding: 15px;
  border-radius: 5px;
  min-height: 300px;
}

.row {
  display: flex;
  flex-wrap: wrap;
}

.details-container {
  flex: 2;
}

.avatar-container {
  flex-basis: 50%;
  background-position: center;
  background-size: contain;
  background-repeat: no-repeat;
}

@media (min-width: 576px) {
  .modal-dialog {
    max-width: 70%;
    margin-right: auto;
    margin-left: auto;
  }
}
</style>
