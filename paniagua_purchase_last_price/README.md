# Paniagua - Actualizar Precio de Compra desde Última Compra

## Descripción

Este módulo actualiza automáticamente el precio de coste (standard_price) de los productos en su ficha basándose en el último precio de compra realizado.

## Funcionalidad

### 🔄 Actualización Automática del Coste

Cada vez que se **confirma un pedido de compra**, el sistema actualiza automáticamente el precio de coste de cada producto con el precio unitario de la compra.

### 📋 Cuándo se actualiza el coste:

1. **Al confirmar un pedido de compra**: Todos los productos del pedido actualizan su coste
2. **Al modificar el precio en un pedido confirmado**: Si cambias el precio de una línea en un pedido ya confirmado, se actualiza el coste
3. **Al agregar líneas a un pedido confirmado**: Si agregas productos a un pedido ya confirmado, se actualiza su coste

### 🎯 Características:

- ✅ **Conversión de UdM**: Si la unidad de medida de compra es diferente a la del producto, se convierte automáticamente
- ✅ **Logging**: Cada actualización queda registrada en los logs con el precio anterior y el nuevo
- ✅ **Automático**: No requiere intervención del usuario
- ✅ **Transparente**: El coste se actualiza sin afectar valoraciones de stock existentes

## Funcionamiento

### Ejemplo:

1. **Producto**: Mesa de madera
   - Coste actual: 50.00 €

2. **Nueva compra**: Creas un pedido de compra
   - Producto: Mesa de madera
   - Precio unitario: 55.00 €

3. **Al confirmar el pedido**:
   - El coste del producto se actualiza automáticamente a 55.00 €
   - Queda registrado en los logs: "Actualizado coste del producto 'Mesa de madera' de 50.00 a 55.00"

4. **Siguiente compra**:
   - Si compras el mismo producto por 52.00 €
   - Al confirmar, el coste se actualiza a 52.00 €

## Consideraciones

- El módulo actualiza el campo `standard_price` del producto
- Solo actualiza cuando el precio de compra es mayor a 0
- Si la compra tiene una UdM diferente a la del producto, convierte el precio automáticamente
- Los pedidos en borrador NO actualizan el coste hasta que se confirman
- El contexto `disable_auto_svl` previene la creación automática de movimientos de valoración

## Instalación

1. Instalar el módulo
2. No requiere configuración adicional
3. Funciona automáticamente desde el momento de la instalación

## Dependencias

- `purchase`: Módulo de compras de Odoo
- `stock`: Módulo de inventario de Odoo

## Autor

Xtendoo - https://www.xtendoo.es

## Licencia

AGPL-3

