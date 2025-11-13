# Paniagua - Control de Impuestos Adicionales en Ventas

## Descripción

Este módulo restringe la capacidad de agregar múltiples impuestos en las líneas de pedido de venta para usuarios que no tengan permisos especiales.

## Funcionalidad

- **Administradores del sistema**: Siempre pueden agregar múltiples impuestos (sin restricciones)
- **Usuarios normales**: Pueden agregar/editar/cambiar UN impuesto en las líneas de venta
- **Usuarios con permisos especiales**: Pueden agregar múltiples impuestos en las líneas de venta

### Comportamiento para usuarios sin permisos:
- ✅ Pueden agregar un impuesto
- ✅ Pueden cambiar/reemplazar el impuesto existente por otro
- ✅ Pueden eliminar el impuesto
- ❌ NO pueden tener más de un impuesto a la vez (si intentan agregar un segundo, automáticamente reemplaza al anterior)

## Configuración

1. Instalar el módulo
2. Ir a **Ajustes > Usuarios y Compañías > Grupos**
3. Buscar el grupo "Puede editar impuestos adicionales en ventas"
4. Añadir los usuarios que deben poder agregar múltiples impuestos

## Uso

- **Administradores**: Sin restricciones, pueden agregar tantos impuestos como necesiten
- **Usuarios normales**:
  - Pueden agregar un primer impuesto
  - Pueden cambiar ese impuesto por otro diferente
  - Si intentan agregar un segundo impuesto adicional, automáticamente se mantiene solo el último seleccionado
- **Usuarios del grupo especial**: Pueden agregar tantos impuestos como necesiten en cada línea de venta

## Validación

El módulo valida automáticamente:
- **En tiempo real** (`@api.onchange`): Si un usuario sin permisos intenta agregar más de un impuesto, automáticamente se queda solo con el último seleccionado
- **Al guardar** (`@api.constrains`): Si de alguna forma se intenta guardar con múltiples impuestos sin permisos → Error

## Autor

Xtendoo - https://www.xtendoo.es

## Licencia

AGPL-3

