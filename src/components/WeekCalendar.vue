<template>
  <div class="calendar">
    <h2>Календарь событий</h2>
    <span v-for="selected of selectedDates" :key="selected.dayId">
      {{ selected.date?.toLocaleDateString() }}
    </span>

    <div class="month">
      <div class="actions">
        <button :disabled="!prevWeekEnabled" @click="prevWeek" class="btn bg-gradient-success btn-sm false false m-2">-</button>

       <span class="m-3"> {{ nameMounth[currentWeek.month] }} - {{ currentWeek.year }}</span>

        <button :disabled="!nextWeekEnabled" @click="nextWeek" class="btn bg-gradient-success btn-sm false false m-2">+</button>
      </div>
      <div class="weeknames grid">
        <span v-for="weekday of weekdays" :key="weekday">{{ weekday }}</span>
      </div>
      <div class="grid">
        <CalendarCell
          v-for="day of currentWeek.days"
          :key="day.dayId"
          :day="day"
          @click="$emit('btn-click',listeners.selectSingle(day))"
        />
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref, watch } from "vue";

import CalendarCell from "@/components/CalendarCell.vue";
import { useCalendar } from "vue-use-calendar";
import { addDays } from "date-fns";
import { ru } from "date-fns/locale";

const nameMounth = [
  "Январь",
  "Февраль",
  "Март",
  "Апрель",
  "Май",
  "Июнь",
  "Июль",
  "Август",
  "Сентябрь",
  "Октябрь",
  "Ноябрь",
  "Декабрь",
];
const disabledDates = [addDays(new Date(), 10)];

const firstDayOfWeek = 1;

const { useWeeklyCalendar, useWeekdays } = useCalendar({
  minDate: new Date(),
  maxDate: addDays(new Date(), 26),
  disabled: disabledDates,
  firstDayOfWeek,
  locale: ru,
  preSelection: [addDays(new Date(), 2)],
});

const {
  currentWeek,
  nextWeek,
  prevWeek,
  prevWeekEnabled,
  nextWeekEnabled,
  listeners,
  selectedDates,
} = useWeeklyCalendar({ fullWeeks: false, infinite: true });

const weekdays = useWeekdays();



watch(selectedDates, (newValue, oldValue) => {
  console.log(selectedDates[0].toLocaleDateString() );
});
</script>

<style scoped>
.calendar {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.actions {
  display: flex;
  justify-content: space-between;
  margin: 10px 200px 0px 200px;
}

.month {
  margin-top: 10px;
}
.weeknames {
  display: inline;
}
.grid {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  justify-items: center;
}
</style>
