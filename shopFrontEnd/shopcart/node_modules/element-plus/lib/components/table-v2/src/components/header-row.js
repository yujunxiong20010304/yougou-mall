'use strict';

Object.defineProperty(exports, '__esModule', { value: true });

var vue = require('vue');
var headerRow = require('../header-row.js');

const TableV2HeaderRow = vue.defineComponent({
  name: "ElTableV2HeaderRow",
  props: headerRow.tableV2HeaderRowProps,
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
      return vue.createVNode("div", {
        "class": props.class,
        "style": style
      }, [Cells]);
    };
  }
});

exports["default"] = TableV2HeaderRow;
//# sourceMappingURL=header-row.js.map
