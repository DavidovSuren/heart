<template>
    <div class="calendar">
    <h2>Календарь событий</h2>
  
      <div class="month">
        <div class="actions">
          <button
            class="btn bg-gradient-success btn-sm false false m-2"
            :disabled="!prevMonthEnabled"
            @click="prevMonth"
          >
            -
          </button>
  
          <span class="m-3">{{ nameMounth[currentMonth.month] }} / {{ currentMonth.year }}</span>
  
          <button
            class="btn bg-gradient-success btn-sm false false m-2"
            :disabled="!nextMonthEnabled"
            @click="nextMonth"
          >
            +
          </button>
        </div>
        <div class="weeknames grid">
          <span
            v-for="weekday of weekdays"
            :key="weekday"
          >{{ weekday }}</span>
        </div>
        <div class="grid">
          <CalendarCell
            v-for="day of currentMonth.days"
            :key="day.dayId"
            :day="day"
            @click="listeners.selectSingle(day)"
          />
        </div>
      </div>
    </div>
  </template>
  
<script lang="ts" setup>
import { ref, watch } from "vue";
import CalendarCell from "@/components/CalendarCell.vue";
import { useCalendar } from "vue-use-calendar";
import { addDays } from 'date-fns';
import { ru } from "date-fns/locale";
import { dateEventStore } from "@/stores/pinia";

const dateEvent = dateEventStore()
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
  
  const firstDayOfWeek = 1;
  
  const years = Array.from(new Array(100)).map((_, i) => 1950 + i);
  
  const { useMonthlyCalendar, useWeekdays } = useCalendar({
    startOn: new Date(2023, 5, 12),
    //disabled: disabledDates,
    firstDayOfWeek,
    locale: ru,
    preSelection: [new Date(2023, 5, 15), addDays(new Date(2023, 5, 15), 6)],
  });
  
  const { nextMonth, prevMonth, currentMonthAndYear, prevMonthEnabled, nextMonthEnabled, currentMonth, listeners, selectedDates } = useMonthlyCalendar({ infinite: true });
  //selectedDates.splice(0, selectedDates.length, ...[new Date(2023, 5, 15), addDays(new Date(2023, 5, 15), 6)]);
  const weekdays = useWeekdays();
  
  function goToCurrentMonth () {
    const today = new Date();
    currentMonthAndYear.month = today.getMonth();
    currentMonthAndYear.year = today.getFullYear();
  }
  goToCurrentMonth()

watch(selectedDates, (newValue, oldValue) => {
  console.log(selectedDates[0])
  dateEvent.day = selectedDates[0].getDate()
  dateEvent.mounth = selectedDates[0].getMonth()+1
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
  
  .row {
    display: flex;
    gap: 8px;
  }
  </style>