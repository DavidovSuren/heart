<script setup>
import MaterialButton from "@/components/MaterialButton.vue";

defineProps({
  image: {
    type: String,
    required: true,
  },
  title: {
    type: String,
    required: true,
  },
  description: {
    type: String,
    required: true,
  },
  action: {
    type: Object,
    color: String,
    route: String,
    label: String,
    default: () => ({
      color: "bg-gradient-success",
      label: "ПЕРЕЙТИ",
    }),
  },
});
</script>
<template>
  <div class="card">
    <div class="card-header p-0 position-relative mt-n4 mx-3 z-index-2">
      <a :href="action.route" class="d-block blur-shadow-image">
        <img :src="image" :alt="title" class="img-fluid border-radius-lg" />
      </a>
    </div>
    <div class="card-body text-center">
      <h5 class="font-weight-normal">
        <a href="javascript:;">{{ title }}</a>
      </h5>


      <MaterialButton
        variant="gradient"
        color="success"
        data-bs-toggle="modal"
        data-bs-target="#exampleModal"
      >
        ПЕРЕЙТИ
      </MaterialButton>
      <!-- Modal -->
      <div
        class="modal fade"
        id="exampleModal"
        tabindex="-1"
        aria-labelledby="exampleModalLabel"
        aria-hidden="true"
      >
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="exampleModalLabel">
                {{ title }}
              </h5>

            </div>
            <div class="modal-body">
              <img
                :src="image"
                :alt="title"
                style="width: 100%; margin: 0.4%; padding: 2%"
              />
              {{ description }}
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
      <!-- End Modal -->
    </div>
  </div>
</template>
