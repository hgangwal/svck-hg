package nestedcond;
class NestedIfFail;
  // Declare class variables
  protected int my_packet, b, c, d, e;

  function void nested_case_logic_if_case_mixed();
   // if (my_packet != null) begin
    if (true) begin
      if (my_packet.get_status() != ERROR) begin
          case (my_packet.get_type())
              NORMAL: begin
                  if (my_packet.get_destination() == BROADCAST) begin
                      // WARNING - Too many levels of nesting
                      send_packet(ALL_RECEIVERS, my_packet.get_payload());
                  end
                  else begin
                    // WARNING - Too many levels of nesting
                    send_packet(my_packet.get_dest(), my_packet.get_payload());
                    if (y > 35) begin
                        $display("Nested Level 5: y is greater than 35");
                    end
                  end
              end
              SPECIAL: begin
                  if (my_packet.get_destination() == BROADCAST) begin
                      // WARNING - Too many levels of nesting
                      send_special(ALL_RECEIVERS, my_packet.get_code());
                  end
                  else begin
                      // WARNING - Too many levels of nesting
                      send_special(my_packet.get_dest(), my_packet.get_code());
                  end
              end
          endcase
      end
      else begin
          handle_error(my_packet);
      end
  end
endfunction: nested_case_logic_if_case_mixed

endclass: NestedIfFail
endpackage: nestedcond