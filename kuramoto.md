# Kuramoto - Turing model

Let us consider $\phi_1,\dots \phi_n$ the phases of $n$ oscillators We can represent the oscillators using the complex representation $e^{i\phi}$. Let us define the center of mass of all phases but the $k$-th one as follows:
%
\begin{equation}
\hat{\phi}_k = \frac{\sum_{j\neq k} e^{ i \phi}}{\vert \vert \sum_{j\neq k} e^{ i \phi} \vert \vert}
\enspace.
\end{equation}%
With this idea, let us define the \textit{conjugate center of mass} as the phase which is just in the opposite side of the complex circle, i.e.
%
\begin{equation}
\tilde{\phi} = \hat{\phi} + \pi
\enspace.
\end{equation}

Using the notion of conjugate center of mass, we define the following dynamic for the phases:
%
\begin{equation}
\frac{ \text{d} \phi_k}{\text{d} t} = \omega + \sin\left( \tilde{\phi}_k - \phi_k \right)
\enspace.
\end{equation}
%
The idea is that each phase will try to synchronize with the conjugate center of mass of the other phases. My intuition says that the stable states will be when the phase are as separated as posible from each other, i.e. forming perfect polyedrons over the complex circle.

Now the interesting question is what happens if we combine this repelent force, or diffusion, with an attracting force (reaction?). Considering $\alpha$ as a parameter, the full dynamic would be given by
%
\begin{equation}
\frac{ \text{d} \phi_k}{\text{d} t} = \omega + \frac{\alpha}{n}\sum_{j\neq k} \sin(\phi_j - \phi_k) + (1-\alpha) \sin\left( \tilde{\phi}_k - \phi_k \right)
\enspace.
\end{equation}
%

For fixing ideas, consider $n=8$. When $alpha=1$ we recover the classic Kuramoto model, and the stable states are when all the phases are equal. When $alpha = 0$ we have the previous model, where if everything goes ok the stable configuration should be when the phases are forming a polyhedron of eight points. I wonder what happen in between. Could it be that for some intermediate values of $alpha$ we end up with smaller polyhedron?

I think because of the sublinearity of the sine, similar phases will pull more than distant ones. Therefore, maybe similar phases will feel a more strong attractive force while the more distant ones will tend to diverge. I feel this would be a interaction very similar to what is found in the Turing patter model, no?
