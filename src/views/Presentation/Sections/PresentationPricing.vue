<script setup>
import SimplePricingCard from "@/examples/cards/pricingCards/SimplePricingCard.vue";
</script>
<template>
  <section class="py-sm-7" id="pricing-soft-ui">
    <div class="bg-gradient-success position-relative mx-n3 overflow-hidden">
      <img
        src="@/assets/img/shapes/pattern-lines.svg"
        alt="pattern-lines"
        class="position-absolute start-0 top-md-0 w-100 opacity-6"
      />
      <div
        class="container pb-lg-8 pb-7 pt-5 postion-relative z-index-2 position-relative"
      >
        <div class="row">
          <div class="col-md-7 mx-auto text-center">
            <span class="badge bg-gradient-dark mb-2">Pricing</span>
            <h3 class="text-white">Ready to get Material Kit?</h3>
            <p class="text-white">
              Based on the license you get, you will have direct access to our
              team <br />
              of developers who built the product.
            </p>
          </div>
        </div>
      </div>
    </div>
    <div class="mt-lg-n8 mt-n6">
      <div class="container">
        <div class="row mt-5">
          <SimplePricingCard
            title="Freelancer"
            description="Good for a personal or client web/mobile app."
            :price="{ currency: '$', amount: '79' }"
            :action="{
              label: 'Бесплатные экскурсии',
              color: 'bg-gradient-dark',
            }"
            :specifications="[
              'Complete documentation',
              'Full code',
              'Projects - 1',
              'Team size - 1',
              'Support',
              'Free Updates - 6 months',
            ]"
          />

          <SimplePricingCard
            title="Startup"
            description="Build your startup or client web/mobile app."
            :price="149"
            :specifications="[
              'Complete documentation',
              'Full code',
              'Projects - 1',
              'Team size - up to 5',
              'Support',
              'Free Updates - 12 months',
            ]"
          />

          <SimplePricingCard
            color="bg-gradient-dark"
            title="Компания"
            description="Perfect for web/mobile apps or SaaS projects."
            :price="249"
            :action="{ route: '', label: 'Бесплатные экскурсии', color: 'btn-white' }"
            :specifications="[
              'Complete documentation',
              'Full code',
              'Use in SaaS',
              'Projects - unlimited',
              'Team Size - up to 20',
              'Priority support',
              'Free Updates - 12 months',
            ]"
          />

          <SimplePricingCard
            title="Enterprise"
            description="Deploy large-scale projects which include redistribution
                    rights."
            :price="599"
            :action="{
              label: 'Бесплатные экскурсии',
              color: 'bg-gradient-dark',
            }"
            :specifications="[
              'Complete documentation',
              'Full code',
              'Use in SaaS',
              'Projects - unlimited',
              'Team Size - more than 20',
              'Priority support',
              'Free Updates - 24 months',
            ]"
          />
        </div>
    </div>
  </section>
</template>
