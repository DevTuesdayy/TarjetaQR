<script setup>
import { computed, ref } from 'vue';
import { useToast } from 'primevue/usetoast';

const toast = useToast();
const products = ref([
    { id: 1, name: 'Impresora LaserJet Color', quantity: 2, unitPrice: 5200 },
    { id: 2, name: 'Monitor LED 31 pulg.', quantity: 3, unitPrice: 1700 }
]);
const productDialog = ref(false);
const deleteDialog = ref(false);
const submitted = ref(false);
const editingProduct = ref(null);
const productForm = ref(createEmptyProduct());

function createEmptyProduct() {
    return { name: '', quantity: 1, unitPrice: null };
}

const subtotal = computed(() => products.value.reduce((total, product) => total + product.quantity * product.unitPrice, 0));
const tax = computed(() => subtotal.value * 0.16);
const total = computed(() => subtotal.value + tax.value);

function formatCurrency(value) {
    return new Intl.NumberFormat('es-MX', { style: 'currency', currency: 'MXN' }).format(value);
}

function openNew() {
    editingProduct.value = null;
    productForm.value = createEmptyProduct();
    submitted.value = false;
    productDialog.value = true;
}

function editProduct(product) {
    editingProduct.value = product;
    productForm.value = { ...product };
    submitted.value = false;
    productDialog.value = true;
}

function saveProduct() {
    submitted.value = true;
    const form = productForm.value;

    if (!form.name?.trim() || !form.quantity || !form.unitPrice) return;

    if (editingProduct.value) {
        Object.assign(editingProduct.value, {
            name: form.name.trim(),
            quantity: form.quantity,
            unitPrice: form.unitPrice
        });
        toast.add({ severity: 'success', summary: 'Producto actualizado', detail: form.name, life: 2500 });
    } else {
        products.value.push({
            id: Date.now(),
            name: form.name.trim(),
            quantity: form.quantity,
            unitPrice: form.unitPrice
        });
        toast.add({ severity: 'success', summary: 'Producto registrado', detail: form.name, life: 2500 });
    }

    productDialog.value = false;
}

function confirmDelete(product) {
    editingProduct.value = product;
    deleteDialog.value = true;
}

function deleteProduct() {
    products.value = products.value.filter((product) => product.id !== editingProduct.value.id);
    deleteDialog.value = false;
    toast.add({ severity: 'success', summary: 'Producto eliminado', detail: editingProduct.value.name, life: 2500 });
    editingProduct.value = null;
}
</script>

<template>
    <div class="pos-page">
        <div class="pos-header">
            <div>
                <span class="eyebrow"><i class="pi pi-shopping-cart" /> Control de ventas</span>
                <h1>Punto de Venta (POS)</h1>
                <p>Registra los productos de la compra y consulta el total a pagar.</p>
            </div>
            <div class="header-icon"><i class="pi pi-calculator" /></div>
        </div>

        <div class="card register-card">
            <div class="card-heading">
                <div>
                    <h2>Productos de la compra</h2>
                    <p>Agrega, edita o elimina productos de esta venta.</p>
                </div>
                <Button label="Registrar producto" icon="pi pi-plus" @click="openNew" />
            </div>

            <DataTable class="pos-table" :value="products" data-key="id" paginator :rows="5" :rows-per-page-options="[5, 10, 20]" responsive-layout="scroll">
                <template #empty>No hay productos registrados.</template>
                <Column header="Cns" style="width: 5rem">
                    <template #body="{ index }">{{ index + 1 }}</template>
                </Column>
                <Column field="name" header="Nombre del producto" sortable>
                    <template #body="{ data }">
                        <div class="product-name">
                            <span class="product-avatar"><i class="pi pi-box" /></span>
                            <span>{{ data.name }}</span>
                        </div>
                    </template>
                </Column>
                <Column field="unitPrice" header="Precio U." sortable>
                    <template #body="{ data }">{{ formatCurrency(data.unitPrice) }}</template>
                </Column>
                <Column field="quantity" header="Cant." sortable />
                <Column header="Precio P." sortable>
                    <template #body="{ data }">{{ formatCurrency(data.quantity * data.unitPrice) }}</template>
                </Column>
                <Column header="Acciones" style="width: 10rem">
                    <template #body="{ data }">
                        <div class="actions">
                            <Button icon="pi pi-pencil" severity="success" rounded aria-label="Editar" @click="editProduct(data)" />
                            <Button icon="pi pi-trash" severity="danger" rounded aria-label="Eliminar" @click="confirmDelete(data)" />
                        </div>
                    </template>
                </Column>
            </DataTable>
        </div>

        <div class="totals-card card">
            <div class="total-item">
                <span>Subtotal</span><strong>{{ formatCurrency(subtotal) }}</strong>
            </div>
            <div class="total-item">
                <span>IVA (16%)</span><strong>{{ formatCurrency(tax) }}</strong>
            </div>
            <div class="total-item total-final">
                <span>Total</span><strong>{{ formatCurrency(total) }}</strong>
            </div>
        </div>

        <Dialog v-model:visible="productDialog" modal :header="editingProduct ? 'Editar producto' : 'Registrar producto'" :style="{ width: '30rem' }">
            <div class="form-grid">
                <div class="field field-wide">
                    <label for="product-name">Nombre del producto</label>
                    <InputText id="product-name" v-model.trim="productForm.name" autofocus placeholder="Ej. Teclado inalámbrico" :invalid="submitted && !productForm.name" />
                    <small v-if="submitted && !productForm.name">Escribe el nombre del producto.</small>
                </div>
                <div class="field">
                    <label for="product-quantity">Cantidad</label>
                    <InputNumber id="product-quantity" v-model="productForm.quantity" :min="1" :use-grouping="false" :invalid="submitted && !productForm.quantity" />
                </div>
                <div class="field">
                    <label for="product-price">Precio unitario</label>
                    <InputNumber id="product-price" v-model="productForm.unitPrice" mode="currency" currency="MXN" locale="es-MX" :min="0.01" :invalid="submitted && !productForm.unitPrice" />
                </div>
            </div>
            <template #footer>
                <Button label="Cancelar" text severity="secondary" @click="productDialog = false" />
                <Button label="Guardar" icon="pi pi-check" @click="saveProduct" />
            </template>
        </Dialog>

        <Dialog v-model:visible="deleteDialog" modal header="Confirmar eliminación" :style="{ width: '30rem' }">
            <p>
                ¿Deseas eliminar <strong>{{ editingProduct?.name }}</strong> de la compra?
            </p>
            <template #footer>
                <Button label="Cancelar" text severity="secondary" @click="deleteDialog = false" />
                <Button label="Eliminar" icon="pi pi-trash" severity="danger" @click="deleteProduct" />
            </template>
        </Dialog>
    </div>
</template>

<style scoped>
.pos-page {
    max-width: 1180px;
    margin: 0 auto;
}
.pos-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 24px;
    margin-bottom: 28px;
    padding: 30px 34px;
    border-radius: 18px;
    color: #fff;
    background: linear-gradient(115deg, #123f72, #1664a3 55%, #1a9db4);
    box-shadow: 0 18px 35px rgba(24, 75, 125, 0.18);
}
.eyebrow {
    display: inline-flex;
    gap: 8px;
    margin-bottom: 10px;
    color: #cceeff;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
}
.pos-header h1 {
    margin: 0;
    color: #ffffff;
    font-size: clamp(26px, 4vw, 38px);
    letter-spacing: -0.04em;
}
.pos-header p {
    margin: 9px 0 0;
    color: #e1f5ff;
    font-size: 14px;
}
.header-icon {
    display: grid;
    place-items: center;
    width: 68px;
    height: 68px;
    border: 1px solid rgba(255, 255, 255, 0.3);
    border-radius: 20px;
    color: #ffffff;
    background: rgba(255, 255, 255, 0.14);
    font-size: 28px;
}
.header-side {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    gap: 12px;
}
.sale-status {
    display: inline-flex;
    align-items: center;
    gap: 7px;
    padding: 7px 11px;
    border: 1px solid #bfe4df;
    border-radius: 999px;
    color: #087b75;
    background: #e8f8f5;
    font-size: 11px;
    font-weight: 700;
}
.sale-status i {
    color: #15aa7e;
    font-size: 7px;
}
.quick-stats {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
    margin: 16px 0 22px;
}
.stat-card {
    display: flex;
    align-items: center;
    gap: 13px;
    padding: 16px 18px;
    border: 1px solid var(--surface-border);
    border-radius: 14px;
    background: var(--surface-card);
    box-shadow: 0 5px 14px rgba(28, 43, 74, 0.04);
}
.stat-card small,
.stat-card strong {
    display: block;
}
.stat-card small {
    margin-bottom: 4px;
    color: var(--text-color-secondary);
    font-size: 11px;
}
.stat-card strong {
    color: var(--text-color);
    font-size: 19px;
}
.stat-icon,
.summary-icon,
.product-avatar {
    display: grid;
    place-items: center;
}
.stat-icon {
    width: 42px;
    height: 42px;
    border-radius: 12px;
    font-size: 17px;
}
.stat-icon.blue {
    color: #2274c9;
    background: #e8f3ff;
}
.stat-icon.purple {
    color: #7752c9;
    background: #f0ebff;
}
.stat-icon.green {
    color: #078d7b;
    background: #e3faf4;
}
.stat-card.highlight {
    border-color: #a9e6da;
    background: #f3fcfa;
}
.card {
    padding: 24px;
    border: 1px solid var(--surface-border);
    border-radius: 16px;
    background: var(--surface-card);
    box-shadow: 0 10px 24px rgba(28, 43, 74, 0.06);
}
.register-card {
    position: relative;
    overflow: hidden;
}
.workspace-grid {
    display: grid;
    grid-template-columns: minmax(0, 1fr) 320px;
    gap: 22px;
    align-items: start;
}
.card-heading {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 20px;
    margin-bottom: 20px;
}
.card-heading h2 {
    margin: 0;
    color: var(--text-color);
    font-size: 21px;
}
.card-heading p {
    margin: 6px 0 0;
    color: var(--text-color-secondary);
    font-size: 13px;
}
.actions {
    display: flex;
    gap: 8px;
}
.product-name {
    display: flex;
    align-items: center;
    gap: 11px;
    font-weight: 600;
}
.product-avatar {
    width: 34px;
    height: 34px;
    border-radius: 10px;
    color: #1677a6;
    background: #e9f7ff;
}
.totals-card {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 18px;
    margin-top: 20px;
}
.summary-icon {
    flex: 0 0 42px;
    width: 42px;
    height: 42px;
    border-radius: 12px;
    color: #087b75;
    background: #e3faf4;
    font-size: 17px;
}
.totals-title h2 {
    margin: 0;
    color: var(--text-color);
    font-size: 16px;
}
.totals-title p {
    margin: 4px 0 0;
    color: var(--text-color-secondary);
    font-size: 11px;
}
.total-item {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 14px;
    padding: 15px 18px;
    border: 1px solid var(--surface-border);
    border-radius: 12px;
    color: var(--text-color-secondary);
}
.total-item strong {
    color: var(--text-color);
    font-size: 18px;
}
.total-final {
    border-color: #79c8de;
    background: #eefaff;
}
.total-final strong {
    color: #12678c;
}
.total-final span {
    color: #12678c;
    font-weight: 700;
}
.form-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 18px;
}
.field {
    display: flex;
    flex-direction: column;
    gap: 7px;
}
.field-wide {
    grid-column: 1 / -1;
}
.field label {
    color: var(--text-color);
    font-weight: 600;
}
.field small {
    color: var(--red-500);
}
.pos-table :deep(.p-datatable-thead > tr > th) {
    color: #547085;
    background: #f7fafc;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.04em;
    text-transform: uppercase;
}
.pos-table :deep(.p-datatable-tbody > tr) {
    transition: background 0.2s ease;
}
.pos-table :deep(.p-datatable-tbody > tr:hover) {
    background: #f5fbff;
}
.pos-table :deep(.p-paginator) {
    border-top: 1px solid var(--surface-border);
    margin-top: 8px;
    padding-bottom: 0;
}
.checkout-card {
    position: sticky;
    top: 24px;
    padding: 22px;
    background: #ffffff;
}
.checkout-heading {
    display: flex;
    align-items: center;
    gap: 12px;
    padding-bottom: 20px;
    border-bottom: 1px solid var(--surface-border);
}
.checkout-heading h2 {
    margin: 0;
    color: var(--text-color);
    font-size: 18px;
}
.customer-row {
    display: flex;
    align-items: center;
    gap: 10px;
    margin: 18px 0;
    padding: 11px;
    border: 1px solid #dcecf4;
    border-radius: 12px;
    background: #f5fbff;
}
.customer-row > i {
    margin-left: auto;
    color: #8aa4b4;
    font-size: 12px;
}
.customer-avatar {
    display: grid;
    place-items: center;
    width: 34px;
    height: 34px;
    border-radius: 10px;
    color: #1775a1;
    background: #dff2fc;
}
.customer-row small,
.customer-row strong {
    display: block;
}
.customer-row small {
    margin-bottom: 3px;
    color: var(--text-color-secondary);
    font-size: 10px;
}
.customer-row strong {
    color: var(--text-color);
    font-size: 13px;
}
.checkout-lines {
    display: grid;
    gap: 13px;
    padding: 3px 0 18px;
    border-bottom: 1px dashed #cbdde7;
}
.checkout-lines div {
    display: flex;
    justify-content: space-between;
    color: var(--text-color-secondary);
    font-size: 13px;
}
.checkout-lines strong {
    color: var(--text-color);
    font-weight: 700;
}
.grand-total {
    display: flex;
    align-items: flex-end;
    justify-content: space-between;
    gap: 10px;
    padding: 20px 0;
}
.grand-total span {
    color: #426477;
    font-size: 13px;
    font-weight: 700;
}
.grand-total strong {
    color: #087b75;
    font-size: 28px;
    letter-spacing: -0.04em;
}
.finish-button {
    width: 100%;
    justify-content: center;
    border: 0;
    background: #078d7b;
    box-shadow: 0 7px 14px rgba(8, 141, 123, 0.16);
}
.finish-button:hover {
    background: #06776a;
}
.secure-note {
    margin: 14px 0 0;
    color: #8299a6;
    font-size: 10px;
    text-align: center;
}
.secure-note i {
    margin-right: 4px;
    color: #18a47f;
}
@media (max-width: 720px) {
    .pos-header {
        align-items: flex-start;
        padding: 24px 22px;
    }
    .header-icon {
        width: 52px;
        height: 52px;
        font-size: 21px;
    }
    .header-side {
        gap: 8px;
    }
    .card-heading {
        align-items: flex-start;
        flex-direction: column;
    }
    .workspace-grid,
    .totals-card,
    .form-grid {
        grid-template-columns: 1fr;
    }
    .checkout-card {
        position: static;
    }
    .quick-stats {
        grid-template-columns: 1fr;
        margin-right: 0;
        margin-left: 0;
    }
    .field-wide {
        grid-column: auto;
    }
}
</style>
