import { SVGAttributes } from "react";

export interface MenuItemSVG extends SVGAttributes<SVGElement> {
  isSelected?: boolean;
}
