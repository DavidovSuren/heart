<script setup>
import MaterialButton from "@/components/MaterialButton.vue";
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
              <div class="modal-header">
                <h5
                  class="modal-title"
                  id="exampleModalLabel"
                  v-html="title"
                ></h5>
                <MaterialButton
                  color="none"
                  class="btn-close"
                  data-bs-dismiss="modal"
                  aria-label="Close"
                >
                </MaterialButton>
              </div>
              <div class="modal-body">
                <span v-html="acf.card_content"></span>
                {{ acf.openHour }}
                {{ acf.openday }}
                {{ acf.openminute }}
                {{ acf.openmounth }}
                {{ acf.price }}
                {{ acf.views }}
                {{ acf.whatsapp }}
                {{ acf.workPeriod }}
                {{ acf.Почта }}
                {{ acf.адрес }}
                {{ acf.видео }}
                {{ acf.вк }}
                {{ acf.время_работы }}
                {{ acf.инстаграм }}
                {{ acf.меню }}
                {{ acf.награды }}
                {{ acf.рейтинг }}
                {{ acf.телеграмм }}
                {{ acf.телефон }}
                <span v-html="description"></span>

                <img :src="img" :alt="description" />
              </div>
              <div class="modal-footer justify-content-between">
                <MaterialButton
                  variant="gradient"
                  color="dark"
                  data-bs-dismiss="modal"
                >
                  Закрыть
                </MaterialButton>
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
</style>
>
