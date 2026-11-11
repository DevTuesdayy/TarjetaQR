<script setup>
const projects = [
    {
        title: 'Credencial Institucional',
        description: 'Genera y consulta tu credencial digital con código QR y código de barras.',
        icon: 'pi pi-id-card',
        to: '/tarjeta',
        status: 'Disponible'
    },
    {
        title: 'Sistema de Ventas',
        description: 'Administra productos, registra operaciones y consulta tus ventas.',
        icon: 'pi pi-shopping-cart',
        to: '/pos',
        status: 'Disponible'
    }
];
</script>

<template>
    <section class="dashboard-home">
        <div class="welcome">
            <div>
                <span class="eyebrow"><i class="pi pi-th-large" /> Panel de proyectos</span>
                <h1>Bienvenido a tu dashboard</h1>
                <p>Accede a tus aplicaciones desde un solo lugar.</p>
            </div>
            <div class="welcome-icon"><i class="pi pi-briefcase" /></div>
        </div>

        <div class="section-heading">
            <div>
                <h2>Mis proyectos</h2>
                <p>Selecciona una aplicación para comenzar.</p>
            </div>
            <span class="project-count">{{ projects.length }} proyectos</span>
        </div>

        <div class="project-grid">
            <router-link v-for="project in projects" :key="project.title" :to="project.to" class="project-card">
                <div class="project-icon"><i :class="project.icon" /></div>
                <div class="project-copy">
                    <span class="project-status">{{ project.status }}</span>
                    <h3>{{ project.title }}</h3>
                    <p>{{ project.description }}</p>
                </div>
                <i class="pi pi-arrow-up-right project-arrow" />
            </router-link>
        </div>
    </section>
</template>

<style scoped>
.dashboard-home {
    max-width: 1180px;
    margin: 0 auto;
}
.welcome {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 20px;
    margin-bottom: 36px;
    padding: 30px 34px;
    border-radius: 18px;
    color: white;
    background: linear-gradient(115deg, #0b536f, #087b8d 55%, #14a78e);
    box-shadow: 0 18px 35px rgba(8, 104, 123, 0.18);
}
.eyebrow {
    display: inline-flex;
    align-items: center;
    gap: 7px;
    margin-bottom: 12px;
    color: #b9fff0;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
}
h1 {
    margin: 0;
    font-size: clamp(26px, 4vw, 38px);
    letter-spacing: -0.04em;
}
.welcome p {
    margin: 9px 0 0;
    color: #d2fff7;
    font-size: 14px;
}
.welcome-icon {
    display: grid;
    place-items: center;
    width: 68px;
    height: 68px;
    border: 1px solid rgba(255, 255, 255, 0.3);
    border-radius: 20px;
    color: white;
    background: rgba(255, 255, 255, 0.14);
    font-size: 28px;
}
.section-heading {
    display: flex;
    align-items: end;
    justify-content: space-between;
    gap: 18px;
    margin-bottom: 18px;
}
h2 {
    margin: 0;
    color: var(--text-color);
    font-size: 22px;
}
.section-heading p {
    margin: 6px 0 0;
    color: var(--text-color-secondary);
    font-size: 13px;
}
.project-count {
    padding: 8px 12px;
    border-radius: 999px;
    color: #087b75;
    background: #e2fbf5;
    font-size: 11px;
    font-weight: 700;
}
.project-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(270px, 1fr));
    gap: 18px;
}
.project-card {
    position: relative;
    display: flex;
    align-items: flex-start;
    gap: 15px;
    min-height: 160px;
    padding: 22px;
    border: 1px solid var(--surface-border);
    border-radius: 16px;
    color: inherit;
    background: var(--surface-card);
    box-shadow: 0 10px 24px rgba(28, 43, 74, 0.06);
    text-decoration: none;
    transition:
        transform 0.2s,
        box-shadow 0.2s,
        border-color 0.2s;
}
.project-card:hover {
    border-color: #68d8c5;
    box-shadow: 0 15px 28px rgba(17, 120, 112, 0.14);
    transform: translateY(-3px);
}
.project-icon {
    display: grid;
    flex: 0 0 44px;
    place-items: center;
    width: 44px;
    height: 44px;
    border-radius: 13px;
    color: #078d7b;
    background: #e3faf4;
    font-size: 20px;
}
.project-copy {
    min-width: 0;
    padding-right: 15px;
}
.project-status {
    color: #078d7b;
    font-size: 10px;
    font-weight: 750;
    letter-spacing: 0.08em;
    text-transform: uppercase;
}
h3 {
    margin: 8px 0 7px;
    color: var(--text-color);
    font-size: 17px;
}
.project-copy p {
    margin: 0;
    color: var(--text-color-secondary);
    font-size: 12px;
    line-height: 1.55;
}
.project-arrow {
    position: absolute;
    top: 22px;
    right: 20px;
    color: #8a99a9;
    font-size: 13px;
}
@media (max-width: 640px) {
    .dashboard-home {
        width: 100%;
    }
    .welcome {
        gap: 14px;
        align-items: flex-start;
        padding: 24px 22px;
    }
    .welcome-icon {
        width: 48px;
        height: 48px;
        font-size: 19px;
    }
    .section-heading {
        align-items: flex-start;
        flex-direction: column;
    }
    .project-grid {
        grid-template-columns: 1fr;
    }
}
</style>
