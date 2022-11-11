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
                {{ acf.фото }}
                {{ acf.openHour }}
                {{ acf.openday }}
                {{ acf.openminute }}
                {{ acf.openmounth }}
                {{ acf.price }}
                {{ acf.whatsapp }}
                {{ acf.workPeriod }}
                {{ acf.Почта }}

                
                <MaterialBadge
                   variant="gradient" 
                   class="btn btn-outline-light">
                    {{ acf.меню }}
                </MaterialBadge>

                <MaterialBadge
                   variant="gradient" 
                   class="btn btn-outline-light">
                   {{ acf.адрес }}
                </MaterialBadge>

                <MaterialBadge 
                   variant="gradient" 
                   class="btn btn-outline-light">
                    {{ acf.видео }}
                </MaterialBadge>

                <MaterialBadge
                   variant="gradient" 
                   color="success">
                   {{ acf.время_работы }}
                </MaterialBadge>

                <MaterialBadge
                   variant="gradient" 
                   color="success">
                   {{ acf.награды }}
                </MaterialBadge>

                <MaterialBadge
                   variant="gradient" 
                   class="btn btn-outline-light">
                   {{ acf.телефон }}
                </MaterialBadge>

                <MaterialBadge
                   variant="gradient" 
                   color="success"
                    rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

                   {{ acf.рейтинг }}
                </MaterialBadge>

                {{ acf.вк }}
                {{ acf.инстаграм }}
                {{ acf.телеграмм }}
                
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
.star-rating{
 font-size: 0;
}
.star-rating__wrap{
 display: inline-block;
 font-size: 1rem;
}
.star-rating__wrap:after{
 content: "";
 display: table;
 clear: both;
}
.star-rating__ico{
 float: right;
 padding-left: 2px;
 cursor: pointer;
 color: #FFB300;
}
.star-rating__ico:last-child{
 padding-left: 0;
}
.star-rating__input{
 display: none;
}
.star-rating__ico:hover:before,
.star-rating__ico:hover ~ .star-rating__ico:before,
.star-rating__input:checked ~ .star-rating__ico:before
{
 content: "\f005";
}
</style>
>
