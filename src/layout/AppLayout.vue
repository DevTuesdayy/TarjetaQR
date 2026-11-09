<script setup>
import { useLayout } from '@/layout/composables/layout';
import { computed } from 'vue';
import { useRoute } from 'vue-router';
import AppFooter from './AppFooter.vue';
import AppSidebar from './AppSidebar.vue';
import AppTopbar from './AppTopbar.vue';

const { layoutConfig, layoutState, hideMobileMenu } = useLayout();
const route = useRoute();
const isDashboard = computed(() => route.name === 'dashboard');

const containerClass = computed(() => {
    return {
        'layout-overlay': layoutConfig.menuMode === 'overlay',
        'layout-static': layoutConfig.menuMode === 'static',
        'layout-overlay-active': layoutState.overlayMenuActive,
        'layout-mobile-active': layoutState.mobileMenuActive,
        'layout-static-inactive': layoutState.staticMenuInactive
    };
});
</script>

<template>
    <div class="layout-wrapper" :class="[containerClass, { 'clean-dashboard': isDashboard }]">
        <AppTopbar v-if="!isDashboard" />
        <AppSidebar v-if="!isDashboard" />
        <div class="layout-main-container" :class="{ 'clean-main-container': isDashboard }">
            <div class="layout-main">
                <router-view />
            </div>
            <AppFooter v-if="!isDashboard" />
        </div>
        <div v-if="!isDashboard" class="layout-mask animate-fadein" @click="hideMobileMenu" />
    </div>
    <Toast />
</template>

<style scoped>
.clean-dashboard { background: var(--surface-ground); }
.clean-main-container { padding: 2rem clamp(1rem, 4vw, 4rem); }

@media (max-width: 640px) {
    .clean-main-container { padding: 1.25rem 1rem; }
}
</style>
