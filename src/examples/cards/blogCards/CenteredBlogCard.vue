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
      <p class="mb-0">
        {{ description }}
      </p>

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
                Your modal title
              </h5>
              <MaterialButton
                color="none"
                class="btn-close"
                data-bs-dismiss="modal"
                aria-label="Close"
              >
              </MaterialButton>
            </div>
            <div class="modal-body"
            ><img src="https://bipbap.ru/wp-content/uploads/2017/04/0_7c779_5df17311_orig.jpg" alt="" style="width: 370px;
  margin: 5%;
  padding: 2%;">
              Society has put up so many boundaries, so many limitations on
              what’s right and wrong that it’s almost impossible to get a pure
              thought out.
              <br /><br />
              It’s like a little kid, a little boy, looking at colors, and no
              one told him what colors are good, before somebody tells you you
              shouldn’t like pink because that’s for girls, or you’d instantly
              become a gay two-year-old.
            </div>
            <div class="modal-footer justify-content-between">
              <MaterialButton
                variant="gradient"
                color="dark"
                data-bs-dismiss="modal"
              >
                Close
              </MaterialButton>
              <MaterialButton variant="gradient" color="success" class="mb-0">
                Save changes
              </MaterialButton>
            </div>
          </div>
        </div>
      </div>
      <!-- End Modal -->
    </div>
  </div>
</template>
