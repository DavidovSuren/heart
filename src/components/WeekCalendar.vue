<template>
  <div class="calendar">
    <h2>Календарь событий</h2>
    Выбор:
    <span v-for="selected of selectedDates" :key="selected.dayId">
      {{ selected.date.toLocaleDateString() }}
    </span>

    <div class="month">
      <div class="actions">
        <button :disabled="!prevWeekEnabled" @click="prevWeek">-</button>

        {{ currentWeek.month + 1 }} - {{ currentWeek.year }} W:{{
          currentWeek.weekNumber + 1
        }}

        <button :disabled="!nextWeekEnabled" @click="nextWeek">+</button>
      </div>
      <div class="weeknames grid">
        <span v-for="weekday of weekdays" :key="weekday">{{ weekday }}</span>
      </div>
      <div class="grid">
        <CalendarCell
          v-for="day of currentWeek.days"
          :key="day.dayId"
          :day="day"
          @click="listeners.selectSingle(day)"
        />
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import CalendarCell from "@/components/CalendarCell.vue";
import { useCalendar } from "vue-use-calendar";
import { addDays } from "date-fns";
import { ru } from "date-fns/locale";

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
} = useWeeklyCalendar();

const weekdays = useWeekdays();
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
  margin: 10px 0;
}

.month {
  margin-top: 16px;
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
