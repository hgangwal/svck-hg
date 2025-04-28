package nestedcond;
class NestedIfGOOD;
  function void nested_case_logic_if_case_mixed();
      if (my_packet.get_status() != ERROR) begin
          case (my_packet.get_type())
              NORMAL: begin
                  if (my_packet.get_destination() == BROADCAST) begin
                      // GOOD -
                      send_packet(ALL_RECEIVERS, my_packet.get_payload());
                  end
                  else begin
                    // GOOD - 
                    send_packet(my_packet.get_dest(), my_packet.get_payload());
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
  endfunction: nested_case_logic_if_case_mixed
endclass: NestedIfGOOD
endpackage: nestedcond