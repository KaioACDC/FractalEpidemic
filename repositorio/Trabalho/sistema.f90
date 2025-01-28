module sistema
    implicit none

contains
    subroutine sistema (t, t_inf, dydt, y, t_rec)
        
        !Parâmetros de entrada
        real(8), intent(in) :: t
        real(8), intent(in) :: t_inf
        real(8), intent(in) :: t_rec
        real(8), intent(in) :: y(3)
        
        !Parâmetros de saída
        real(8), intent(out) :: dydt

        dydt(1) = -t_inf * y(1) * y(2)
        dydt(2) = t_inf * y(1) * y(2) - t_rec * y(2)
        dydt(3) = t_rec * y(2)
    end subroutine sistema

    subroutine kutta_sistema(delta_t, y0, t_inf, t_rec, pt, y_saida, t_saida)
        
