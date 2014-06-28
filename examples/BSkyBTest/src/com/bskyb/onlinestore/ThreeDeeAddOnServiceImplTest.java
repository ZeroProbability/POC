package com.bskyb.onlinestore;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;
import static org.mockito.Matchers.anyString;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

import java.util.Set;

import org.junit.Test;
import org.mockito.Mockito;

import com.acme.serviceavailability.AvailabilityChecker;
import com.acme.serviceavailability.TechnicalFailureException;

public class ThreeDeeAddOnServiceImplTest {

	@Test
	public void testNoPostCode() throws Exception {
		AvailabilityChecker ac = mock(AvailabilityChecker.class);
		ThreeDeeAddOnService service = new ThreeDeeAddOnServiceImpl(new ACMESkyAvailabilityChecker(ac));

		Set<ProductCodes3D> ret = service.checkFor3DAddOnProducts(new Basket(),
				null);
		assertTrue(ret.isEmpty());
	}

	@Test(expected = InvalidPostcodeException.class)
	public void testInvalidPostCode() throws Exception {
		final String invalidCode = "XYZ";
		AvailabilityChecker ac = mock(AvailabilityChecker.class);
		when(ac.isPostCodeIn3DTVServiceArea(invalidCode)).thenReturn(
				AvailabilityReturnCodes.POSTCODE_INVALID.name());

		ThreeDeeAddOnService service = new ThreeDeeAddOnServiceImpl(new ACMESkyAvailabilityChecker(ac));

		service.checkFor3DAddOnProducts(new Basket(), invalidCode);
	}

	@Test
	public void testServiceThrowsException() throws Exception {
		AvailabilityChecker ac = mock(AvailabilityChecker.class);

		Mockito.doThrow(new TechnicalFailureException()).when(ac)
				.isPostCodeIn3DTVServiceArea(anyString());

		ThreeDeeAddOnService service = new ThreeDeeAddOnServiceImpl(new ACMESkyAvailabilityChecker(ac));
		Set<ProductCodes3D> ret = service.checkFor3DAddOnProducts(new Basket(
				ProductCodes.NEWS.name(), ProductCodes.KIDS.name(),
				ProductCodes.SPORTS.name()), "SOME_POST_CODE");
		assertTrue(ret.isEmpty());

	}

	private void testServiceCommon(String retString) throws Exception {
		final String plannedCode = "XYZ";
		AvailabilityChecker ac = mock(AvailabilityChecker.class);
		when(ac.isPostCodeIn3DTVServiceArea(plannedCode)).thenReturn(retString);

		ThreeDeeAddOnService service = new ThreeDeeAddOnServiceImpl(new ACMESkyAvailabilityChecker(ac));

		Set<ProductCodes3D> ret = service.checkFor3DAddOnProducts(new Basket(),
				plannedCode);

		assertTrue(ret.isEmpty());

		ret = service.checkFor3DAddOnProducts(
				new Basket(ProductCodes.NEWS.name(), ProductCodes.KIDS.name(),
						ProductCodes.SPORTS.name()), plannedCode);

		assertTrue(ret.isEmpty());
	}

	@Test
	public void testServicePlanned() throws Exception {
		testServiceCommon(AvailabilityReturnCodes.SERVICE_PLANNED.name());
	}

	@Test
	public void testServiceUnavailable() throws Exception {
		testServiceCommon(AvailabilityReturnCodes.SERVICE_UNAVAILABLE.name());
	}

	@Test
	public void test3DProductsNotInBasket() throws Exception {
		AvailabilityChecker ac = mock(AvailabilityChecker.class);
		when(ac.isPostCodeIn3DTVServiceArea(anyString())).thenReturn(
				AvailabilityReturnCodes.SERVICE_AVAILABLE.name());

		ThreeDeeAddOnService service = new ThreeDeeAddOnServiceImpl(new ACMESkyAvailabilityChecker(ac));

		Set<ProductCodes3D> ret = service.checkFor3DAddOnProducts(new Basket(
				ProductCodes.KIDS.name()), "SOME_POST_CODE");

		assertTrue(ret.isEmpty());
	}

	@Test
	public void test3DProductsInBasket() throws Exception {
		AvailabilityChecker ac = mock(AvailabilityChecker.class);
		when(ac.isPostCodeIn3DTVServiceArea(anyString())).thenReturn(
				AvailabilityReturnCodes.SERVICE_AVAILABLE.name());

		ThreeDeeAddOnService service = new ThreeDeeAddOnServiceImpl(new ACMESkyAvailabilityChecker(ac));

		Set<ProductCodes3D> ret = service.checkFor3DAddOnProducts(new Basket(
				ProductCodes.MOVIES_1.name()), "SOME_POST_CODE");

		assertEquals(ret.size(), 1);
		assertTrue(ret.contains(ProductCodes3D.MOVIES_3D_ADD_ON));

		ret = service.checkFor3DAddOnProducts(
				new Basket(ProductCodes.NEWS.name(), ProductCodes.KIDS.name(),
						ProductCodes.SPORTS.name()), "SOME_POST_CODE");

		assertEquals(ret.size(), 2);
		assertTrue(ret.contains(ProductCodes3D.SPORTS_3D_ADD_ON));
		assertTrue(ret.contains(ProductCodes3D.NEWS_3D_ADD_ON));
	}

}
