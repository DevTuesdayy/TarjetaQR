<script setup>
import { ref } from 'vue';
import AppMenuItem from './AppMenuItem.vue';

const model = ref([
    {
        label: 'UNIVERSIDAD AUTÓNOMA DE CHIAPAS',
        items: [
            {
                label: 'Dashboard',
                icon: 'pi pi-fw pi-home',
                to: '/dashboard'
            }
        ]
    },
    {
        label: 'MÓDULOS',
        items: [
            {
                label: 'Credencial "Práctica 1"',
                icon: 'pi pi-fw pi-id-card',
                to: '/tarjeta'
            },
            {
                label: 'Punto de Venta "Práctica 2"',
                icon: 'pi pi-fw pi-shopping-cart',
                to: '/pos'
            },
            {
                label: 'Graficas',
                icon: 'pi pi-fw pi-chart-bar',
                to: '/uikit/charts'
            },
            {
                label: 'Input',
                icon: 'pi pi-fw pi-check-square',
                to: '/uikit/input'
            },
            {
                label: 'Float Label',
                icon: 'pi pi-fw pi-bookmark',
                to: '/uikit/formlayout'
            },
            {
                label: 'Invalid State',
                icon: 'pi pi-fw pi-exclamation-circle',
                to: '/uikit/input'
            },
            {
                label: 'Button',
                icon: 'pi pi-fw pi-mobile',
                to: '/uikit/button'
            },
            {
                label: 'Table',
                icon: 'pi pi-fw pi-table',
                to: '/uikit/table'
            },
            {
                label: 'List',
                icon: 'pi pi-fw pi-list',
                to: '/uikit/list'
            },
            {
                label: 'Tree',
                icon: 'pi pi-fw pi-share-alt',
                to: '/uikit/tree'
            },
            {
                label: 'Panel',
                icon: 'pi pi-fw pi-tablet',
                to: '/uikit/panel'
            }
        ]
    }
]);
</script>

<template>
    <ul class="layout-menu">
        <template v-for="(item, i) in model" :key="item.label">
            <app-menu-item :item="item" :index="i" />
        </template>
    </ul>
</template>

<style lang="scss" scoped></style>
