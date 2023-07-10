<template>
  <div class="star-rating">
    <span v-for="i in maxStars" :key="i" @click="selectStar(i)" :class="{ 'filled': i <= selectedStar }">
      ★
    </span>
  </div>
</template>

<script>
export default {
  props: {
    value: {
      type: Number,
      required: true,
      validator: (value) => {
        return value >= 1 && value <= 5;
      },
    },
  },
  data() {
    return {
      selectedStar: this.value,
      maxStars: 5,
    };
  },
  methods: {
    selectStar(star) {
      this.selectedStar = star;
      this.$emit('update:value', star);
    },
  },
};
</script>

<style scoped>
.star-rating {
  font-size: 24px!important;
}

.filled {
  color: gold;
}
</style>