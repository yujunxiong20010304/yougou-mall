import { defineComponent, createVNode } from 'vue';
import { tableV2HeaderRowProps } from '../header-row.mjs';

const TableV2HeaderRow = defineComponent({
  name: "ElTableV2HeaderRow",
  props: tableV2HeaderRowProps,
  setup(props, {
    slots
  }) {
    return () => {
      const {
        columns,
        headerIndex,
        style
      } = props;
      let Cells = columns.map((column, columnIndex) => {
        return slots.cell({
          columns,
          column,
          columnIndex,
          headerIndex
        });
      });
      if (slots.header) {
        Cells = slots.header({
          cells: Cells,
          columns,
          headerIndex
        });
      }
      return createVNode("div", {
        "class": props.class,
        "style": style
      }, [Cells]);
    };
  }
});

export { TableV2HeaderRow as default };
//# sourceMappingURL=header-row.mjs.map
