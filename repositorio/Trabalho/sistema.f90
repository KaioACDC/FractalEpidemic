module sistema
    implicit none

contains
    subroutine sistema_e_d(t, y, dydt, t_inf, t_rec)
        
        !Parâmetros de entrada
        real(8), intent(in) :: t
        real(8), intent(in) :: t_inf
        real(8), intent(in) :: t_rec
        real(8), intent(in) :: y(3)
        
        !Parâmetros de saída
        real(8), intent(out) :: dydt(3)
        

        dydt(1) = -t_inf * y(1) * y(2)
        dydt(2) = t_inf * y(1) * y(2) - t_rec * y(2)
        dydt(3) = t_rec * y(2)

    end subroutine sistema_e_d

    subroutine kutta_sistema(delta_t, y0, t_inf, t_rec, pt, y_saida, t_saida)
        
        !Parâmetros de entrada
        real(8), intent(in) :: delta_t(2)
        real(8), intent(in) :: t_inf
        real(8), intent(in) :: t_rec
        real(8), intent(in) :: y0(3)
        integer, intent(in) :: pt

        !Parâmetros de saída
        real(8), intent(out) :: t_saida(pt)
        real(8), intent(out) :: y_saida(3, pt)

        !Variáveis locais
        real(8) :: h, t, y(3)
        real(8) :: k1(3), k2(3), k3(3), k4(3)
        integer :: i

        h = (delta_t(2) - delta_t(1)) / (pt - 1)

        t = delta_t(1)
        y = y0
        t_saida(1) = t
        y_saida(:, 1) = y

        !Para resolver o sistema em todos os passos de tempo
        do i = 2, pt
            !Método de Runge-Kutta de 4 ordem
            call sistema_e_d(t, y, k1, t_inf, t_rec)
            call sistema_e_d(t + 0.5*h, y + 0.5*h*k1, k2, t_inf, t_rec)
            call sistema_e_d(t + 0.5*h, y + 0.5*h*k2, k3, t_inf, t_rec)
            call sistema_e_d(t + h, y + h*k3, k4, t_inf, t_rec)

            y = y + (h/6.0)*(k1 + 2*k2 + 2*k3 + k4)
            t = t + h

            t_saida(i) = t 
            y_saida(:, i) = y

        end do
    end subroutine kutta_sistema
end module sistema