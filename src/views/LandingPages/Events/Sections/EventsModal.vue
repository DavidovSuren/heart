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
  date: {
    type: String,
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
                      <div class="col">
                        <p class="date">{{ date }}</p>
                      </div>
                      <div class="col">
                        <p>{{ description }}</p>
                      </div>
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

.date {
  font-weight: bold;
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
