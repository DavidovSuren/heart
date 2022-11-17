<script setup>
//Vue Material Kit 2 components
</script>
<template>
  <div class="container">
    <div class="row mt-5">
      <div class="col-sm-3 col-6 mx-auto">
        <!-- Button trigger modal -->


        <!-- Modal -->
        <div
          class="modal fade"
          id="excursionsModal"
          tabindex="-1"
          aria-labelledby="exampleModalLabel"
          aria-hidden="true"
        >
          <div class="modal-dialog">
            <div class="modal-content">
              <div>
            
                <MaterialButton
                  color="none"
                  class="btn-close"
                  data-bs-dismiss="modal"
                  aria-label="Close">
                </MaterialButton>
              </div>
              <div class="modal-body" color="green"
              ><img src="@/assets/img/adm.jpeg" style="margin-left: 80px; margin-right: auto; width: 300px" >
              <h5 class="modal-title" id="exampleModalLabel">
                  Администрация города-курорта Кисловодск 
                </h5>
                Предоставляет 30 бесплатных билетов, на пешеходную экскурсию по исторической части города курорта Кисловодска еженедельно, успей забрать.<br><br>
               Свяжись в 
      <a href="https://wa.me/89187835805>"
                   data-action="share/whatsapp/share">WhatsApp</a>
                <br />+79187835805
              </div>
              <div class="modal-footer justify-content-between">
                <MaterialButton
                  variant="gradient"
                  color="dark"
                  data-bs-dismiss="modal">
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
