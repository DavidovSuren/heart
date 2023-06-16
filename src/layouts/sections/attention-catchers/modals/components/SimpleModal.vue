<script setup>
import { computed } from "vue";
import MaterialButton from "@/components/MaterialButton.vue";

const modalProps = defineProps({
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
  openHour: {
    type: String,
  },
  workPeriod: {
    type: String,
  },
  content: {
    type: Object,
  },
  gallery: {
    type: Object,
  },
  photos: {
    type: Object,
  },   
  whatsapp: {
    type: String,
  },
  card_content: {
    type: String,
  },
  video: {
    type: String,
  },
  menu: {
    type: String,
  },  
  rating: {
    type: Number,
  },
  address: {
    type: String,
  },
  phone: {
    type: String,
  },  
});
const clouseHour = computed(() => {
  return (modalProps.openHour + modalProps.workPeriod) % 24; // date.getHours() < openHour.value + workPeriod.value ? 'green' : 'red'
});
const isOpen = computed(() => {
  const date = new Date();
  return date.getHours() &&
    date.getHours() < modalProps.openHour + modalProps.workPeriod
    ? 1
    : 0;
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
                    class="avatar-container col-6 col-sm-12 col-md-6 col-lg-6 col-xl-5"
                    :style="`background-image: url(${img});`"
                  ></div>
                  <div class="details-container col-6 col-sm-12 col-md-6 col-lg-6 col-xl-7">
                    <div class="content">
                      <h3 v-html="title"></h3>
                      <vue3-star-ratings
                        starSize="32"
                        showControl="false"
                        disableClick="true"
                        value="rating"
                      />

                      <div class="col">
                        <p class="pTime sTitle" v-if="openHour && workPeriod">
                          <i v-if="isOpen" class="material-icons text-gradient text-success text-2xl">done</i>
                          <span style="color: red" v-if="!isOpen">
                            Закрыто
                          </span>
                          {{ openHour }}:00 -{{ clouseHour }}:00
                        </p>
                        <p class="pTime sTitle" v-if="!openHour">
                          {{ opentime }}
                        </p>
                      </div>

                      <p v-html="card_content"></p>

                      {{ whatsapp }}

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
                  v-if="video"
                >
                  <a :href="`${video}`" target="_blank"> Видео </a>
                </MaterialButton>
                <a v-if="menu" :href="`${menu}`" target="_blank">
                  <img
                    src="@/assets/img/Меню.png"
                    style="width: 80px; height: 80px"
                /></a>
                <MaterialButton
                  variant="outline"
                  color="info"
                  class="w-auto me-2"
                  v-if="address"
                >
                  <a :href="`https://www.google.com/maps/dir//${address}`" target="_blank">
                    {{ address }}
                  </a>
                </MaterialButton>
                <MaterialButton
                  variant="outline"
                  color="info"
                  class="w-auto me-2"
                  v-if="phone"
                >
                  <a :href="`tel:${phone}`">{{phone }}</a>
                </MaterialButton>
              </div>

              <div class="modal-footer justify-content-between">
                <img
                  v-for="img in photos"
                  :src="img.photo"
                  :alt="img.alt"
                  :key="img.id"
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
  min-height: 36vh;
  width: 100%;
  background-position: center;
  background-size: contain;
  background-repeat: no-repeat;
}


</style>
